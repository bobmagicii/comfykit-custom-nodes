
import os
import comfy.sd
import folder_paths

"""
provide a typecasting block to help with the nodes from other packages that
can take dynamic things. sometimes nodes like that will fail to set themselves
up the first load of a workflow if they are also fed from a dynamic output node.
putting one of these in the chain will help those link up knowing their input
types.
"""

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


