
class City(object):

    def __init__(self, 
        id: str = '',
        city: str = '',
        currency: str = '',
        currencySymbol: str = '',
        country: str = '',
        state: str = '',
        currencyAbbr: str = '',
        currencyAbbrText: str = '',
        distanceMetrics: str = '',
        distanceMetricsUnit: float = 0,
        radiusforsomeOneElseBooking: float = 0,
        maxEtaDistanceInMeters: float = 0,
        maxEtaTimeInSeconds: float = 0,
        isTipEnable: bool = '',
        tipType: float = 0,
        paymentMode: object = {},
        paymentGateways: dict = [],
        isCorporateEnable: bool = '',
        isFavoriteDriverEnable: bool = '',
        isDeleted: bool = '',
        location: object = {},
        timeOffset: str = '',
        polygons: object = {},
        pointsProps: object = {},
        dstOffset: str = '',
        timeZoneId: str = '',
        walletSettings: object = {},
        isPreferenceEnabled: bool = '',
        cityStatus: str = ''

    ):
        self.id = id
        self.city = city
        self.currency = currency
        self.currencySymbol = currencySymbol
        self.country = country
        self.state = state
        self.currencyAbbr = currencyAbbr
        self.currencyAbbrText = currencyAbbrText
        self.distanceMetrics = distanceMetrics
        self.distanceMetricsUnit = distanceMetricsUnit
        self.radiusforsomeOneElseBooking = radiusforsomeOneElseBooking
        self.maxEtaDistanceInMeters = maxEtaDistanceInMeters
        self.maxEtaTimeInSeconds = maxEtaTimeInSeconds
        self.isTipEnable = isTipEnable
        self.tipType = tipType
        self.paymentMode = paymentMode
        self.paymentGateways = paymentGateways
        self.isCorporateEnable = isCorporateEnable
        self.isFavoriteDriverEnable = isFavoriteDriverEnable
        self.isDeleted = isDeleted
        self.location = location
        self.timeOffset = timeOffset
        self.polygons = polygons
        self.pointsProps = pointsProps
        self.dstOffset = dstOffset
        self.timeZoneId = timeZoneId
        self.walletSettings = walletSettings
        self.isPreferenceEnabled = isPreferenceEnabled
        self.cityStatus = cityStatus