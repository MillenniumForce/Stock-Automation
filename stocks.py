from dataclasses import dataclass

@dataclass
class StockDef:
	company: str
	ticker: str
	desiredPrice: float

stock_list = [
	StockDef("Lepidico", "LPD.AX", 0.084),
	StockDef("Whispir", "WSP.AX", 5.12),
	StockDef("Openpay", "OPY.AX", 4.88),
	StockDef("Zip Co", "Z1P.AX", 8.00),
	StockDef("Appen", "APX.AX", 13.19)
]


# For Testing:
# stock_list = [StockDef("Lepidico", "LPD.AX", 0.001), StockDef("Whispiro", "WSP.AX", 0.001)]
