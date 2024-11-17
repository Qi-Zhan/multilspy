"""
Configuration parameters for Multilspy.
"""

from enum import Enum
from dataclasses import dataclass


class Language(str, Enum):
    """
    Possible languages with Multilspy.
    """

    CSHARP = "csharp"
    PYTHON = "python"
    RUST = "rust"
    JAVA = "java"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"

    def extension(self) -> str:
        match self:
            case Language.PYTHON: return ".py"
            case Language.CSHARP: return ".cs"
            case Language.RUST: return ".rs"
            case Language.JAVA: return ".java"
            case Language.TYPESCRIPT: return ".ts"
            case Language.JAVASCRIPT: return ".js"

    def tree_sitter(self):
        import tree_sitter
        match self:
            case Language.PYTHON:
                import tree_sitter_python
                return tree_sitter.Language(tree_sitter_python.language())
            case _: raise NotImplementedError()

    def __str__(self) -> str:
        return self.value


@dataclass
class MultilspyConfig:
    """
    Configuration parameters
    """
    code_language: Language
    trace_lsp_communication: bool = False

    @classmethod
    def from_dict(cls, env: dict):
        """
        Create a MultilspyConfig instance from a dictionary
        """
        import inspect
        return cls(**{
            k: v for k, v in env.items()
            if k in inspect.signature(cls).parameters
        })
