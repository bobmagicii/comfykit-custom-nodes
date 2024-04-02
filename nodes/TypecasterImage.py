
import os
import comfy.sd
import folder_paths

class TypecasterImage:

	def __init__(self):
		pass

	RETURN_TYPES = ("IMAGE", )
	RETURN_NAMES = ("IMAGE", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	Bumper = 1

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"image": ("IMAGE", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, image):

		return (image, )


