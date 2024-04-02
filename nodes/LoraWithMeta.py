
import os
import comfy.sd
import folder_paths

class LoraWithMeta:

	def __init__(self):
		pass

	RETURN_TYPES = ("MODEL", "CLIP", "STRING")
	RETURN_NAMES = ("MODEL", "CLIP", "TRIGGERS")

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	Bumper = 1

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		loraList = folder_paths.get_filename_list("loras")
		loraList.insert(0, "None")

		fieldPreset = ("INT", {
			"default": 0, "min": 0, "max": 99,
			"step": 1, "display": "number"
		})

		fieldStr = ("FLOAT", {
			"default": 1.0, "min": -16.0, "max": 16.0,
			"step": 0.1, "display": "number"
		})

		output = { "required": {
			"model": ("MODEL", ),
			"clip": ("CLIP", ),
			"lora1": (loraList, ),
			"lora1_tgr_preset": fieldPreset,
			"lora1_str_model": fieldStr,
			"lora1_str_clip": fieldStr,
			"lora2": (loraList, ),
			"lora2_tgr_preset": fieldPreset,
			"lora2_str_model": fieldStr,
			"lora2_str_clip": fieldStr,
			"lora3": (loraList, ),
			"lora3_tgr_preset": fieldPreset,
			"lora3_str_model": fieldStr,
			"lora3_str_clip": fieldStr
		} }

		return output

	################################################################
	################################################################

	@classmethod
	def IS_CHANGED(
		self, model, clip,
		lora1, lora1_tgr_preset, lora1_str_model, lora1_str_clip,
		lora2, lora2_tgr_preset, lora2_str_model, lora2_str_clip,
		lora3, lora3_tgr_preset, lora3_str_model, lora3_str_clip
	):

		##self.Bumper += self.Bumper

		return self.Bumper

	################################################################
	################################################################

	def onRun(
		self, model, clip,
		lora1, lora1_tgr_preset, lora1_str_model, lora1_str_clip,
		lora2, lora2_tgr_preset, lora2_str_model, lora2_str_clip,
		lora3, lora3_tgr_preset, lora3_str_model, lora3_str_clip
	):

		l1 = { "name": lora1, "tp": lora1_tgr_preset, "sm": lora1_str_model, "sc": lora1_str_clip }
		l2 = { "name": lora2, "tp": lora2_tgr_preset, "sm": lora2_str_model, "sc": lora2_str_clip }
		l3 = { "name": lora3, "tp": lora3_tgr_preset, "sm": lora3_str_model, "sc": lora3_str_clip }

		mblend, cblend = self.applyLoraStack(
			model, clip, [ l1, l2, l3 ]
		)

		tblend = self.fetchLoraTriggers(
			[ l1, l2, l3 ]
		)

		return (mblend, cblend, tblend)

	def applyLoraStack(self, model, clip, listOfLora):

		mblend = model
		cblend = clip

		########

		for lora in listOfLora:
			if(lora['name'] == "None"):
				continue

			lpath = folder_paths.get_full_path("loras", lora['name'])
			lfile = comfy.utils.load_torch_file(lpath, safe_load=True)
			mblend, cblend = comfy.sd.load_lora_for_models(mblend, cblend, lfile, lora['sm'], lora['sc'])
			print(f"[LoRA+Metadata Apply] {lpath}, {lora['sm']}, {lora['sc']}")

		########

		return (mblend, cblend)

	def fetchLoraTriggers(self, listOfLora):

		output = []

		########

		for lora in listOfLora:
			if(lora['name'] == 'None'):
				continue

			if(lora['tp'] <= 0):
				continue

			lpath = folder_paths.get_full_path('loras', lora['name'])
			lpath = lpath.replace('.safetensors', f".tp{lora['tp']:02d}.txt")

			if(not os.path.isfile(lpath)):
				print(f'[LoRA+Metadata Triggers] Preset Not Found: {lpath}')
				continue

			print(f'[LoRA+Metadata Triggers] {lpath}')

			lfile = open(lpath, 'r')
			output.append(lfile.readline())
			lfile.close()

		########

		return ', '.join(output)

