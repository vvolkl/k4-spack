
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class K4reccalorimeter(CMakePackage, Key4hepPackage):
    """Generator components for the Key4hep framework"""
    homepage = "https://github.com/HEP-FCC/k4RecCalorimeter/"
    url      = "https://github.com/HEP-FCC/k4RecCalorimeter/archive/v0.16.tar.gz"
    git      = "https://github.com/HEP-FCC/k4RecCalorimeter.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version("0.1.0pre01", tag="v0.1.0pre01")

    generator = 'Ninja'

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('ninja', type='build')
    depends_on("edm4hep")
    depends_on('k4fwcore@1:')
    depends_on("dd4hep +geant4")
    depends_on("fccdetectors")

    # todo: remove when ready
    depends_on("fcc-edm")

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
        spack_env.set("K4RECCALORIMETER", self.prefix.share.k4RecCalorimeter)
