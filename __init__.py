from .nodes.LoraStackFiveSimple import *

from .nodes.TypecasterClip import *
from .nodes.TypecasterCond import *
from .nodes.TypecasterImage import *
from .nodes.TypecasterLatent import *
from .nodes.TypecasterModel import *
from .nodes.TypecasterVae import *

# these are depreciated i just dont want some of my older flows to die
# before i can update them.
from .nodes.LoraWithMeta import *
from .nodes.LoraThree import *

NODE_CLASS_MAPPINGS = {
	"TypecasterClip": TypecasterClip,
	"TypecasterCond": TypecasterCond,
	"TypecasterImage": TypecasterImage,
	"TypecasterLatent": TypecasterLatent,
	"TypecasterModel": TypecasterModel,
	"TypecasterVae": TypecasterVae,

	"LoraStackFiveSimple": LoraStackFiveSimple,

	"LoraWithMeta": LoraWithMeta,
	"LoraThree": LoraThree
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"TypecasterClip": "Recast CLIP",
	"TypecasterCond": "Recast Conditioning",
	"TypecasterImage": "Recast Image",
	"TypecasterLatent": "Recast Latent",
	"TypecasterModel": "Recast Model",
	"TypecasterVae": "Recast VAE",
	"LoraStackFiveSimple": "LoRA S5"
}

__all__ = [ 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS' ]
