from typing import Literal

from SilvaViridis.Python.Common.Types import NonEmptyString

from ._DirectivesList import DIR_AUTH_JWT
from ...Common import DirectiveBase, OnOff, Variable

class AuthJwt(DirectiveBase):
    def __init__(
        self,
        realm : NonEmptyString | Literal[OnOff.off] = OnOff.off,
        token : Variable | None = None,
    ):
        super().__init__(DIR_AUTH_JWT)

        if isinstance(realm, OnOff):
            self.add_arg(realm)
        else:
            self.add_arg(realm)
            self.add_arg(token, "token=")
