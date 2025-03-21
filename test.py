from SilvaViridis.Python.Common.Web import HttpMethod, HttpStatus

from src.SilvaViridis.Exe.NginxConfBuilder.Common import *
from src.SilvaViridis.Exe.NginxConfBuilder.Generators import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.Core import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.HttpAccess import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.HttpAuthBasic import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.HttpAuthJwt import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.HttpCore import *
from src.SilvaViridis.Exe.NginxConfBuilder.Modules.HttpCore.Variables import *

# absolute_redirect  = AbsoluteRedirect()

# aio = Aio("threads")

# client_body_temp_path = ClientBodyTempPath(
#     path = Path("some_path"),
#     levels = [1, 3],
# )

# directio = Directio()

limit_except = LimitExcept([HttpMethod.GET, HttpMethod.POST], [
    Allow(Access.all),
    Deny(Access.all),
    AuthBasic(),
    AuthBasicUserFile(Path("path")),
    AuthJwt(),
    AuthJwtKeyFile(Path("file")),
    AuthJwtKeyRequest(Path("uri")),
    AuthJwtType(),
    AuthJwtRequire(VAR_CONNECTION, error = HttpStatus.Forbidden),
])

# open_file_cache = OpenFileCache(2)

server_name = ServerName()

# types = Types()

auth_jwt = AuthJwt("gf ertet")

auth_jwt_claim_set = AuthJwtClaimSet(Variable("email"), ["info", "e-mail", "job title"])

gen = CrossplaneGenerator()

print(gen.build_many([
    # absolute_redirect,
    # aio,
    # client_body_temp_path,
    # directio,
    limit_except,
    # open_file_cache,
    server_name,
    # types,
    auth_jwt,
    auth_jwt_claim_set,
]))
