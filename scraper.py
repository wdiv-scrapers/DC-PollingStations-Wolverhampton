from dc_base_scrapers.arcgis_scraper import ArcGisScraper

districts_url = "https://maps.wolverhampton.gov.uk/arcgis/rest/services/PollingDistrictsStations/MapServer/1/query?where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson"
stations_url = "https://maps.wolverhampton.gov.uk/arcgis/rest/services/PollingDistrictsStations/MapServer/0/query?where=OBJECTID+LIKE+%27%25%27&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=pjson"
council_id = 'WLV'


stations_scraper = ArcGisScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
