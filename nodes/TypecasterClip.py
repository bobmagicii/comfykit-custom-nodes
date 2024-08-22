
import os
import comfy.sd
import folder_paths

class TypecasterClip:

	def __init__(self):
		pass

	RETURN_TYPES = ("CLIP", )
	RETURN_NAMES = ("CLIP", )

	FUNCTION = "onRun"
	CATEGORY = "bobmagicii"

	################################################################
	################################################################

	@classmethod
	def INPUT_TYPES(s):

		inputs = { "required": {
			"clip": ("CLIP", )
		} }

		return inputs

	################################################################
	################################################################

	def onRun(self, clip):

		return (clip, )


