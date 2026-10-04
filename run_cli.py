"""碳纤维全流程碳账本命令行冒烟入口。"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from carbon_ledger import CarbonStatement


def main() -> None:
    item = CarbonStatement(**{'statement_code': 'statement-code-001', 'batch_code': 'batch-code-001', 'boundary_version': 'boundary-version-001', 'state': 'draft'})
    print(json.dumps({"item": asdict(item), "fingerprint": item.fingerprint()}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
