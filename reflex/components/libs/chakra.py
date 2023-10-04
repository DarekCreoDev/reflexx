"""Components that are based on Chakra-UI."""
from typing import List

from reflex.components.component import Component
from reflex.utils import imports
from reflex.vars import ImportVar, Var


class ChakraComponent(Component):
    """A component that wraps a Chakra component."""

    library = "@chakra-ui/react@^2.6.0"
    lib_dependencies: List[str] = [
        "@chakra-ui/system@^2.5.6",
        "framer-motion@^10.16.4",
        "@emotion/styled@^11.10.6",
    ]

    def _get_app_wrap_components(self) -> dict[tuple[int, str], Component]:
        return {
            **super()._get_app_wrap_components(),
            (60, "ChakraProvider"): ChakraProvider.create(),
        }


class Global(Component):
    library = "@emotion/react@^11.10.6"
    lib_dependencies: List[str] = [
        "@emotion/styled@^11.10.6",
    ]

    tag = "Global"

    styles: Var[str]


class ChakraProvider(ChakraComponent):
    tag = "ChakraProvider"

    theme: Var[str]

    @classmethod
    def create(cls) -> Component:
        return super().create(
            Global.create(styles=Var.create("GlobalStyles", is_local=False)),
            theme=Var.create("extendTheme(theme)", is_local=False),
        )

    def _get_imports(self) -> imports.ImportDict:
        imports = super()._get_imports()
        imports.setdefault(self.library, set()).add(
            ImportVar(tag="extendTheme", is_default=False),
        )
        imports.setdefault("/utils/theme", set()).add(
            ImportVar(tag="theme", is_default=False),
        )
        imports.setdefault(Global.create().library, set()).add(
            ImportVar(tag="css", is_default=False),
        )
        return imports

    def _get_custom_code(self) -> str | None:
        return """
import '/styles/styles.css'

const GlobalStyles = css`
  /* Hide the blue border around Chakra components. */
  .js-focus-visible :focus:not([data-focus-visible-added]) {
    outline: none;
    box-shadow: none;
  }
`;
"""

    def _get_app_wrap_components(self) -> dict[tuple[int, str], Component]:
        return {
            (50, "ChakraColorModeProvider"): ChakraColorModeProvider.create(),
        }


class ChakraColorModeProvider(ChakraComponent):
    tag = "ChakraColorModeProvider"

    def _get_imports(self) -> imports.ImportDict:
        return {
            self.library: {
                ImportVar(
                    tag="useColorMode", alias="chakraUseColorMode", is_default=False
                ),
            },
            "react": {
                ImportVar(tag="useEffect", is_default=False),
            },
            "/utils/context.js": {
                ImportVar(tag="ColorModeContext", is_default=False),
            },
            "next-themes@^0.2.0": {
                ImportVar(tag="useTheme", is_default=False),
            },
        }

    def _get_custom_code(self) -> str | None:
        return """
function ChakraColorModeProvider({ children }) {
  const {colorMode, toggleColorMode} = chakraUseColorMode()
  const {theme, setTheme} = useTheme()

  useEffect(() => {
    if (colorMode != theme) {
        toggleColorMode()
    }
  }, [theme])

  return (
    <ColorModeContext.Provider value={[ colorMode, toggleColorMode ]}>
      {children}
    </ColorModeContext.Provider>
  )
}"""

    def _get_app_wrap_components(self) -> dict[tuple[int, str], Component]:
        return {}
