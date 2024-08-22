
import os
import comfy.sd
import folder_paths

# provides a widget allowing for the selection of up to 5 loras with a single
# weight that gets applied to both the model and clip as i never found myself
# purposely desyncing those and netting any obvious gains.

class LoraStackFiveSimple:

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

		fieldStr = ("FLOAT", {
			"default": 1.0, "min": -16.0, "max": 16.0,
			"step": 0.1, "display": "number"
		})

		output = { "required": {
			"model": ("MODEL", ),
			"clip": ("CLIP", ),
			"lora1_mdl": (loraList, ),
			"lora1_str": fieldStr,
			"lora2_mdl": (loraList, ),
			"lora2_str": fieldStr,
			"lora3_mdl": (loraList, ),
			"lora3_str": fieldStr,
			"lora4_mdl": (loraList, ),
			"lora4_str": fieldStr,
			"lora5_mdl": (loraList, ),
			"lora5_str": fieldStr
		} }

		return output

	################################################################
	################################################################

	@classmethod
	def IS_CHANGED(
		self, model, clip,
		lora1_mdl, lora1_str, lora2_mdl, lora2_str, lora3_mdl, lora3_str,
		lora4_mdl, lora4_str, lora5_mdl, lora5_str
	):

		##self.Bumper += self.Bumper

		return self.Bumper

	################################################################
	################################################################

	def onRun(
		self, model, clip,
		lora1_mdl, lora1_str, lora2_mdl, lora2_str, lora3_mdl, lora3_str,
		lora4_mdl, lora4_str, lora5_mdl, lora5_str
	):

		l1 = { "name": lora1_mdl, "str": lora1_str }
		l2 = { "name": lora2_mdl, "str": lora2_str }
		l3 = { "name": lora3_mdl, "str": lora3_str }
		l4 = { "name": lora4_mdl, "str": lora4_str }
		l5 = { "name": lora5_mdl, "str": lora5_str }

		mblend, cblend = self.applyLoraStack(
			model, clip, [ l1, l2, l3, l4, l5 ]
		)

		tblend = self.fetchLoraTriggers(
			[ l1, l2, l3, l4, l5 ]
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
			mblend, cblend = comfy.sd.load_lora_for_models(mblend, cblend, lfile, lora['str'], lora['str'])
			print(f"[LoRA+Metadata Apply] {lpath}, {lora['str']}, {lora['str']}")

		########

		return (mblend, cblend)

	def fetchLoraTriggers(self, listOfLora):

		output = []

		########

		for lora in listOfLora:
			if(lora['name'] == 'None'):
				continue

			lpath = folder_paths.get_full_path('loras', lora['name'])
			lpath = lpath.replace('.safetensors', '.txt')

			if(not os.path.isfile(lpath)):
				print(f'[LoRA+Metadata Triggers] Preset Not Found: {lpath}')
				continue

			print(f'[LoRA+Metadata Triggers] {lpath}')

			lfile = open(lpath, 'r')
			output.append(lfile.readline())
			lfile.close()

		########

		return ', '.join(output)

