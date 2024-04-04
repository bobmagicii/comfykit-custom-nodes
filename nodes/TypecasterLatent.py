
import os
import comfy.sd
import folder_paths

class TypecasterLatent:

	def __init__(self):
		pass

	RETURN_TYPES = ("LATENT", )
	RETURN_NAMES = ("LATENT", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"latent": ("LATENT", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, latent):

		return (latent, )


