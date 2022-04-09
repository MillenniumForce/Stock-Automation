from dataclasses import dataclass

@dataclass
class StockDef:
	company: str
	ticker: str
	desiredPrice: float

stock_list = [
	StockDef("Lepidico", "LPD.AX", 0.084),
	StockDef("Whispir", "WSP.AX", 2.56),
	StockDef("Openpay", "OPY.AX", 2.44),
	StockDef("Zip Co", "Z1P.AX", 4.00),
	StockDef("Appen", "APX.AX", 13.19),
	StockDef("Allkem", "AKE.AX", 13.00)
]


# For Testing:
# stock_list = [StockDef("Lepidico", "LPD.AX", 0.001), StockDef("Whispiro", "WSP.AX", 0.001)]
