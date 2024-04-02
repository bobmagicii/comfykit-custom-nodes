from .nodes.LoraWithMeta import *
from .nodes.TypecasterImage import *

NODE_CLASS_MAPPINGS = {
	"LoraWithMeta": LoraWithMeta,
	"TypecasterImage": TypecasterImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"LoraWithMeta": "LoRA+Metadata",
	"Recast Image": TypecasterImage
}

__all__ = [ 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS' ]
