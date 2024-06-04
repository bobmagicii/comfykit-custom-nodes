
import os
import comfy.sd
import folder_paths
import json

################################################################################
################################################################################

class LoraConfig:

	name = ''
	preset = 1
	mstr = 1.0
	cstr = 1.0

	def __init__(self, name, preset, mstr, cstr):

		self.name = name
		self.preset = preset
		self.mstr = mstr
		self.cstr = cstr

		self.log(f'{self.name}, {self.preset}, {self.mstr}, {self.cstr}');

		return


	def log(self, msg):

		print(f'[bobmagicii:LoraConfig] {msg}')

		return

################################################################################
################################################################################

class LoraThree:

	CATEGORY = "bobmagicii"
	FUNCTION = "onRun"

	RETURN_TYPES = ("MODEL", "CLIP", "STRING")
	RETURN_NAMES = ("MODEL", "CLIP", "TRIGGERS")

	Bumper = 1

	################################################################
	################################################################

	@staticmethod
	def FetchLoraFileList():

		out = folder_paths.get_filename_list("loras")

		return out

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(cls):

		loras = cls.FetchLoraFileList()
		loras.insert(0, "None")

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
			"lora1": (loras, ),
			"lora1_tgr_preset": fieldPreset,
			"lora1_str_model": fieldStr,
			"lora1_str_clip": fieldStr,
			"lora2": (loras, ),
			"lora2_tgr_preset": fieldPreset,
			"lora2_str_model": fieldStr,
			"lora2_str_clip": fieldStr,
			"lora3": (loras, ),
			"lora3_tgr_preset": fieldPreset,
			"lora3_str_model": fieldStr,
			"lora3_str_clip": fieldStr
		} }

		return output

	################################################################
	################################################################

	@classmethod
	def IS_CHANGED(
		cls, model, clip,
		lora1, lora1_tgr_preset, lora1_str_model, lora1_str_clip,
		lora2, lora2_tgr_preset, lora2_str_model, lora2_str_clip,
		lora3, lora3_tgr_preset, lora3_str_model, lora3_str_clip
	):

		##self.Bumper += self.Bumper

		return self.Bumper

	################################################################
	################################################################

	def __init__(self):
		pass

	################################################################
	################################################################

	def onRun(
		self, model, clip,
		lora1, lora1_tgr_preset, lora1_str_model, lora1_str_clip,
		lora2, lora2_tgr_preset, lora2_str_model, lora2_str_clip,
		lora3, lora3_tgr_preset, lora3_str_model, lora3_str_clip
	):

		lindex = [
			LoraConfig(lora1, lora1_tgr_preset, lora1_str_model, lora1_str_clip),
			LoraConfig(lora2, lora2_tgr_preset, lora2_str_model, lora2_str_clip),
			LoraConfig(lora3, lora3_tgr_preset, lora3_str_model, lora3_str_clip)
		]

		# read the preset files to generate a list of all the triggers
		# defined by the selected lora.

		tblend = self.fetchLoraTriggers(lindex)

		# apply the stack of loras to the model.

		mblend, cblend = self.applyLoraStack(model, clip, lindex)

		########

		return (mblend, cblend, tblend)

	################################################################
	################################################################

	def applyLoraStack(self, model, clip, lindex: list):

		mblend = model
		cblend = clip

		# loop over all the supplied loras to blend them into the original
		# model and clip.

		lora: LoraConfig

		for lora in lindex:
			if(lora.name == "None"):
				continue

			self.log(f"Apply LoRA: {lora.name}, {lora.mstr}, {lora.cstr}")

			lpath = folder_paths.get_full_path("loras", lora.name)
			lfile = comfy.utils.load_torch_file(lpath, safe_load=True)

			mblend, cblend = comfy.sd.load_lora_for_models(
				mblend, cblend,
				lfile, lora.mstr, lora.cstr
			)

		########

		return (mblend, cblend)

	def fetchLoraTriggers(self, listOfLora):

		output = []

		########

		for lora in listOfLora:
			if(lora.name == 'None'):
				continue

			if(lora.preset <= 0):
				continue

			lpath = folder_paths.get_full_path('loras', lora.name)
			lpath = lpath.replace('.safetensors', f".tp{lora.preset:02d}.txt")

			if(not os.path.isfile(lpath)):
				self.log(f'{lora.name} preset not found {lora.preset}')
				continue

			self.log(f'{lora.name} preset {lpath}')

			lfile = open(lpath, 'r')
			output.append(lfile.readline())
			lfile.close()

		########

		return ', '.join(output)

	################################################################
	################################################################

	def log(self, msg):

		print(f'[bobmagicii:LoraThree] {msg}')

		return

