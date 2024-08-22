
import os
import comfy.sd
import folder_paths

class TypecasterCond:

	def __init__(self):
		pass

	RETURN_TYPES = ("CONDITIONING", )
	RETURN_NAMES = ("CONDITIONING", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"conditioning": ("CONDITIONING", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, conditioning):

		return (conditioning, )


