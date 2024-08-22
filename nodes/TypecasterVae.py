
import os
import comfy.sd
import folder_paths

class TypecasterVae:

	def __init__(self):
		pass

	RETURN_TYPES = ("VAE", )
	RETURN_NAMES = ("VAE", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"vae": ("VAE", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, vae):

		return (vae, )


