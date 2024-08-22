
import os
import comfy.sd
import folder_paths
import json

# deprecated 2024-08-22
# do not use anymore.

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

		out = folder_paths.get_filename_list('loras')

		return out

	@staticmethod
	def FetchLoraPresetList():

		paths = folder_paths.folder_names_and_paths['loras']
		exts = set([ '.txt', '.preset' ])
		out = set()

		for path in paths[0]:
			files, fall = folder_paths.recursive_search(path)
			out.update(folder_paths.filter_files_extensions(
				files, exts
			))

		return sorted(list(out))

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(cls):

		loras = cls.FetchLoraFileList()
		loras.insert(0, 'None')

		presets = cls.FetchLoraPresetList()
		presets.insert(0, 'None')

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
			'l1_preset': (presets, ),
			"l1_mstr": fieldStr,
			"l1_cstr": fieldStr,
			"lora2": (loras, ),
			'l2_preset': (presets, ),
			"l2_mstr": fieldStr,
			"l2_cstr": fieldStr,
			"lora3": (loras, ),
			'l3_preset': (presets, ),
			"l3_mstr": fieldStr,
			"l3_cstr": fieldStr,
		} }

		return output

	################################################################
	################################################################

	@classmethod
	def IS_CHANGED(
		cls, model, clip,
		lora1, l1_preset, l1_mstr, l1_cstr,
		lora2, l2_preset, l2_mstr, l2_cstr,
		lora3, l3_preset, l3_mstr, l3_cstr
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
		lora1, l1_preset, l1_mstr, l1_cstr,
		lora2, l2_preset, l2_mstr, l2_cstr,
		lora3, l3_preset, l3_mstr, l3_cstr
	):

		lindex = [
			LoraConfig(lora1, l1_preset, l1_mstr, l1_cstr),
			LoraConfig(lora2, l2_preset, l2_mstr, l2_cstr),
			LoraConfig(lora3, l3_preset, l3_mstr, l3_cstr)
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

			if(lora.preset == 'None'):
				continue

			lpath = folder_paths.get_full_path('loras', lora.preset)

			if(not os.path.isfile(lpath)):
				self.log(f'{lora.name} preset not found {lora.preset}')
				continue

			self.log(f'{lora.name} preset {lpath}')

			lfile = open(lpath, 'r')
			line = lfile.readline()
			output.append(f'({line})')
			lfile.close()

		########

		return ', \n\n'.join(output)

	################################################################
	################################################################

	def log(self, msg):

		print(f'[bobmagicii:LoraThree] {msg}')

		return

