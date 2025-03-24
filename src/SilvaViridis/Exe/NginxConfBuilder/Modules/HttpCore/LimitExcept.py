from collections.abc import Sequence

from SilvaViridis.Python.Common.Types import NonEmptySequence
from SilvaViridis.Python.Common.Web import HttpMethod

from ._DirectivesList import DIR_LIMIT_EXCEPT
from ..HttpAccess import Allow, Deny
from ..HttpAuthBasic import AuthBasic, AuthBasicUserFile
from ..HttpAuthJwt import AuthJwt, AuthJwtKeyFile, AuthJwtKeyRequest, AuthJwtType, AuthJwtRequire
from ...Common import DirectiveBase

type AccessDirective = Allow | Deny | AuthBasic | AuthBasicUserFile | AuthJwt | AuthJwtKeyFile | AuthJwtKeyRequest | AuthJwtType | AuthJwtRequire

class LimitExcept(DirectiveBase):
    def __init__(
        self,
        methods : NonEmptySequence[HttpMethod],
        access_list : Sequence[AccessDirective] = [],
    ):
        super().__init__(DIR_LIMIT_EXCEPT)

        for method in methods:
            self.add_arg(method.name)

        for directive in access_list:
            self.add_directive(directive)
