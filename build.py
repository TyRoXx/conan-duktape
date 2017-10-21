import platform
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="duktape:shared", pure_c=True)
    if platform.system() == "Windows":  # Library not prepared to create a .lib to link with
        # Remove shared builds in Windows
        static_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            if not ("duktape:shared" in options and options["duktape:shared"]):
                static_builds.append([settings, options, env_vars, build_requires])

        builder.builds = static_builds
    builder.run()
