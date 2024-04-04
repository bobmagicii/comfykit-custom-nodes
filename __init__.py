from .nodes.LoraWithMeta import *
from .nodes.TypecasterImage import *
from .nodes.TypecasterLatent import *

NODE_CLASS_MAPPINGS = {
	"LoraWithMeta": LoraWithMeta,
	"TypecasterImage": TypecasterImage,
	"TypecasterLatent": TypecasterLatent
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"LoraWithMeta": "LoRA+Metadata",
	"Recast Image": TypecasterImage,
	"Recast Latent": TypecasterLatent
}

__all__ = [ 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS' ]
