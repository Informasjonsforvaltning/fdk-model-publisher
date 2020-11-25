data_services_catalog_ttl_mock = """
@prefix dct:   <http://purl.org/dc/terms/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix dcat:  <http://www.w3.org/ns/dcat#> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

<https://dataservices.staging.fellesdatakatalog.digdir.no/catalogs/b0559a91-948a-398b-8052-71e1adaaf877>
        a                  dcat:CatalogRecord ;
        dct:identifier     "b0559a91-948a-398b-8052-71e1adaaf877" ;
        dct:issued         "2020-10-28T08:37:22.773Z"^^xsd:dateTime ;
        dct:modified       "2020-10-28T08:37:22.773Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://dataservice-publisher.staging.fellesdatakatalog.digdir.no/catalogs/80ce530d-628f-4023-a0c9-1ab8797cc190> .

<https://dataservices.staging.fellesdatakatalog.digdir.no/dataservices/7b0758e8-71a3-3a3e-a18b-a9afa3a3e75d>
        a                  dcat:CatalogRecord ;
        dct:identifier     "7b0758e8-71a3-3a3e-a18b-a9afa3a3e75d" ;
        dct:isPartOf       <https://dataservices.staging.fellesdatakatalog.digdir.no/catalogs/b0559a91-948a-398b-8052-71e1adaaf877> ;
        dct:issued         "2020-10-28T08:37:22.773Z"^^xsd:dateTime ;
        dct:modified       "2020-10-28T08:37:22.773Z"^^xsd:dateTime ;
        foaf:primaryTopic  <https://dataservice-publisher.staging.fellesdatakatalog.digdir.no/dataservices/e8acebc9-8743-464b-b002-01ae24291433> .

<https://dataservice-publisher.staging.fellesdatakatalog.digdir.no/dataservices/e8acebc9-8743-464b-b002-01ae24291433>
        a                         dcat:DataService ;
        dct:conformsTo            <https://data.norge.no/specification/kontoopplysninger> ;
        dct:description           "Open API specification of the Account APIs. (Work in progress.)"@en ;
        dct:publisher             <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/937891245> ;
        dct:title                 "Accounts API Skagerrak Sparebank"@en ;
        dcat:endpointDescription  <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> ;
        dcat:endpointURL          <https://test.com> ;
        dcat:mediaType            <https://www.iana.org/assignments/media-types/application/json> , <https://www.iana.org/assignments/media-types/application/jose> .

<https://dataservice-publisher.staging.fellesdatakatalog.digdir.no/catalogs/80ce530d-628f-4023-a0c9-1ab8797cc190>
        a                dcat:Catalog ;
        dct:description  "Samling av kontoopplysnings API"@nb ;
        dct:publisher    <https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/991825827> ;
        dct:title        "DSOP API katalog"@nb ;
        dcat:service     <https://dataservice-publisher.staging.fellesdatakatalog.digdir.no/dataservices/e8acebc9-8743-464b-b002-01ae24291433> .
    """
