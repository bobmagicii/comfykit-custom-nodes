from .nodes.LoraWithMeta import *
from .nodes.LoraThree import *
from .nodes.TypecasterImage import *
from .nodes.TypecasterLatent import *

NODE_CLASS_MAPPINGS = {
	"LoraWithMeta": LoraWithMeta,
	"LoraThree": LoraThree,
	"TypecasterImage": TypecasterImage,
	"TypecasterLatent": TypecasterLatent
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"LoraWithMeta": "[Deprecated] LoRA+Metadata",
	"LoraThree": "LoRA3",
	"Recast Image": TypecasterImage,
	"Recast Latent": TypecasterLatent
}

__all__ = [ 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS' ]
