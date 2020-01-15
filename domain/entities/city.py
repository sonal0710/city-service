
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
        distanceMetricsUnit: int = '',
        radiusforsomeOneElseBooking: int = '',
        maxEtaDistanceInMeters: int = '',
        maxEtaTimeInSeconds: int = '',
        isTipEnable: bool = '',
        tipType: int = '',
        paymentMode: object = {},
        paymentGateways: dict = [],
        isCorporateEnable: bool = '',
        isFavoriteDriverEnable: bool = '',
        isDeleted: bool = '',
        location: object = {},
        timeOffset: int = '',
        polygons: object = {},
        pointsProps: object = {},
        dstOffset: str = '',
        timeZoneId: str = '',
        walletSettings: object = {},
        isPreferenceEnabled: bool = '',
        cityStatus: str = ''

    ):
        if id: self.id = id
        if city: self.city = city
        if currency: self.currency = currency
        if currencySymbol: self.currencySymbol = currencySymbol
        if country: self.country = country
        if state: self.state = state
        if currencyAbbr: self.currencyAbbr = currencyAbbr
        if currencyAbbrText: self.currencyAbbrText = currencyAbbrText
        if distanceMetrics: self.distanceMetrics = distanceMetrics
        if distanceMetricsUnit: self.distanceMetricsUnit = distanceMetricsUnit
        if radiusforsomeOneElseBooking: self.radiusforsomeOneElseBooking = radiusforsomeOneElseBooking
        if maxEtaDistanceInMeters: self.maxEtaDistanceInMeters = maxEtaDistanceInMeters
        if maxEtaTimeInSeconds: self.maxEtaTimeInSeconds = maxEtaTimeInSeconds
        if isTipEnable: self.isTipEnable = isTipEnable
        if tipType: self.tipType = tipType
        if paymentMode: self.paymentMode = paymentMode
        if paymentGateways: self.paymentGateways = paymentGateways
        if isCorporateEnable: self.isCorporateEnable = isCorporateEnable
        if isFavoriteDriverEnable: self.isFavoriteDriverEnable = isFavoriteDriverEnable
        if isDeleted: self.isDeleted = isDeleted
        if location: self.location = location
        if timeOffset: self.timeOffset = timeOffset
        if polygons: self.polygons = polygons
        if pointsProps: self.pointsProps = pointsProps
        if dstOffset: self.dstOffset = dstOffset
        if timeZoneId: self.timeZoneId = timeZoneId
        if walletSettings: self.walletSettings = walletSettings
        if isPreferenceEnabled: self.isPreferenceEnabled = isPreferenceEnabled
        if cityStatus: self.cityStatus = cityStatus