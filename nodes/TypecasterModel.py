
import os
import comfy.sd
import folder_paths

class TypecasterModel:

	def __init__(self):
		pass

	RETURN_TYPES = ("MODEL", )
	RETURN_NAMES = ("MODEL", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"model": ("MODEL", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, model):

		return (model, )


