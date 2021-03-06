# -*- coding: utf-8 -*-

from odata import ODataService
from odata.property import StringProperty, IntegerProperty, DecimalProperty, \
    NavigationProperty, DatetimeProperty

url = 'http://unittest.server.local/odata/'
Service = ODataService(url)


class Product(Service.Base):
    id = IntegerProperty('ProductID', primary_key=True)
    name = StringProperty('ProductName')
    category = StringProperty('Category')
    price = DecimalProperty('Price')


class ProductPart(Service.Base):
    __odata_type__ = 'ODataTest.Objects.ProductPart'
    __odata_collection__ = 'ProductParts'
    id = IntegerProperty('PartID', primary_key=True)
    name = StringProperty('PartName')
    size = DecimalProperty('Size')
    product_id = IntegerProperty('ProductID')


class Manufacturer(Service.Base):
    __odata_type__ = 'ODataTest.Objects.Manufacturer'
    __odata_collection__ = 'Manufacturers'

    id = IntegerProperty('ManufacturerID', primary_key=True)
    name = StringProperty('Name')
    established_date = DatetimeProperty('DateEstablished')


class ProductWithNavigation(Product):
    __odata_type__ = 'ODataTest.Objects.ProductWithNavigation'
    __odata_collection__ = 'ProductsWithNavigation'

    manufacturer_id = IntegerProperty('ManufacturerID')

    manufacturer = NavigationProperty('Manufacturer', Manufacturer, foreign_key=manufacturer_id)
    parts = NavigationProperty('Parts', ProductPart, collection=True)

ProductPart.product = NavigationProperty('Product', ProductWithNavigation, foreign_key=ProductPart.product_id)
