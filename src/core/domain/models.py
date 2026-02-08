from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict

@dataclass
class KnowledgeBase:
    id: str
    name: str
    provider: str
    description: Optional[str] = None
    data_sources: List[Dict[str, Any]] = field(default_factory=list)
