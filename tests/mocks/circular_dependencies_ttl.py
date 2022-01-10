"""Example JSON input."""
# flake8: noqa

circular_dependencies_test_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Catalog>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ConceptSchema>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Contact>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#DataTheme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Dataset>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Distribution>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#HarvestMetadata>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Hits>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PeriodOfTime>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PublisherHit>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Reference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Subject>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Hits> a modelldcatno:ObjectType ;
    dct:title "Hits"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Hits#hits> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#boolean> a modelldcatno:SimpleType ;
    dct:title "boolean"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#dataset> a modelldcatno:Role ;
    dct:title "dataset"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Dataset> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#language> a modelldcatno:Attribute ;
    dct:title "language"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#themeTaxonomy> a modelldcatno:Attribute ;
    dct:title "themeTaxonomy"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#versioninfo> a modelldcatno:Attribute ;
    dct:title "versioninfo"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#versionnumber> a modelldcatno:Attribute ;
    dct:title "versionnumber"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#email> a modelldcatno:Attribute ;
    dct:title "email"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#fullname> a modelldcatno:Attribute ;
    dct:title "fullname"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#hasTelephone> a modelldcatno:Attribute ;
    dct:title "hasTelephone"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#hasURL> a modelldcatno:Attribute ;
    dct:title "hasURL"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#organizationName> a modelldcatno:Attribute ;
    dct:title "organizationName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#organizationUnit> a modelldcatno:Attribute ;
    dct:title "organizationUnit"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#conceptSchema> a modelldcatno:Role ;
    dct:title "conceptSchema"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ConceptSchema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#numberOfHits> a modelldcatno:Attribute ;
    dct:title "numberOfHits"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#pickedDate> a modelldcatno:Attribute ;
    dct:title "pickedDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#startUse> a modelldcatno:Attribute ;
    dct:title "startUse"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accessRights> a modelldcatno:Role ;
    dct:title "accessRights"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accessRightsComment> a modelldcatno:Attribute ;
    dct:title "accessRightsComment"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accrualPeriodicity> a modelldcatno:Role ;
    dct:title "accrualPeriodicity"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#admsIdentifier> a modelldcatno:Attribute ;
    dct:title "admsIdentifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#catalog> a modelldcatno:Role ;
    dct:title "catalog"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Catalog> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#contactPoint> a modelldcatno:Role ;
    dct:title "contactPoint"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Contact> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#descriptionFormatted> a modelldcatno:Attribute ;
    dct:title "descriptionFormatted"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#distribution> a modelldcatno:Role ;
    dct:title "distribution"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Distribution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#harvest> a modelldcatno:Role ;
    dct:title "harvest"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#HarvestMetadata> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasAccuracyAnnotation> a modelldcatno:Role ;
    dct:title "hasAccuracyAnnotation"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasAvailabilityAnnotation> a modelldcatno:Role ;
    dct:title "hasAvailabilityAnnotation"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasCompletenessAnnotation> a modelldcatno:Role ;
    dct:title "hasCompletenessAnnotation"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasCurrentnessAnnotation> a modelldcatno:Role ;
    dct:title "hasCurrentnessAnnotation"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasRelevanceAnnotation> a modelldcatno:Role ;
    dct:title "hasRelevanceAnnotation"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#informationModel> a modelldcatno:Role ;
    dct:title "informationModel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#keyword> a modelldcatno:Attribute ;
    dct:title "keyword"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#landingPage> a modelldcatno:Attribute ;
    dct:title "landingPage"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#language> a modelldcatno:Role ;
    dct:title "language"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForAccess> a modelldcatno:Role ;
    dct:title "legalBasisForAccess"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForProcessing> a modelldcatno:Role ;
    dct:title "legalBasisForProcessing"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForRestriction> a modelldcatno:Role ;
    dct:title "legalBasisForRestriction"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#objective> a modelldcatno:Attribute ;
    dct:title "objective"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#page> a modelldcatno:Attribute ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#provenance> a modelldcatno:Role ;
    dct:title "provenance"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#provenanceSort> a modelldcatno:Attribute ;
    dct:title "provenanceSort"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#references> a modelldcatno:Role ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Reference> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#sample> a modelldcatno:Role ;
    dct:title "sample"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Distribution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#spatial> a modelldcatno:Role ;
    dct:title "spatial"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#subject> a modelldcatno:Role ;
    dct:title "subject"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Subject> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#temporal> a modelldcatno:Role ;
    dct:title "temporal"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PeriodOfTime> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#theme> a modelldcatno:Role ;
    dct:title "theme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#DataTheme> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#accessURL> a modelldcatno:Attribute ;
    dct:title "accessURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#downloadURL> a modelldcatno:Attribute ;
    dct:title "downloadURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#format> a modelldcatno:Attribute ;
    dct:title "format"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#license> a modelldcatno:Role ;
    dct:title "license"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#openLicense> a modelldcatno:Attribute ;
    dct:title "openLicense"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#page> a modelldcatno:Role ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#changed> a modelldcatno:Attribute ;
    dct:title "changed"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#firstHarvested> a modelldcatno:Attribute ;
    dct:title "firstHarvested"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#lastChanged> a modelldcatno:Attribute ;
    dct:title "lastChanged"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#lastHarvested> a modelldcatno:Attribute ;
    dct:title "lastHarvested"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Hits#hits> a modelldcatno:Role ;
    dct:title "hits"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PublisherHit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#endDate> a modelldcatno:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#startDate> a modelldcatno:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#children> a modelldcatno:Role ;
    dct:title "children"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PublisherHit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#hasBody> a modelldcatno:Attribute ;
    dct:title "hasBody"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#inDimension> a modelldcatno:Attribute ;
    dct:title "inDimension"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#motivatedBy> a modelldcatno:Attribute ;
    dct:title "motivatedBy"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Reference#referenceType> a modelldcatno:Role ;
    dct:title "referenceType"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Reference#source> a modelldcatno:Role ;
    dct:title "source"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#extraType> a modelldcatno:Attribute ;
    dct:title "extraType"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#altLabel> a modelldcatno:Attribute ;
    dct:title "altLabel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#creator> a modelldcatno:Role ;
    dct:title "creator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#datasets> a modelldcatno:Role ;
    dct:title "datasets"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Dataset> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#definition> a modelldcatno:Attribute ;
    dct:title "definition"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#inScheme> a modelldcatno:Attribute ;
    dct:title "inScheme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#note> a modelldcatno:Attribute ;
    dct:title "note"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Catalog> a modelldcatno:ObjectType ;
    dct:title "Catalog"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#dataset>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#issued>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#language>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#modified>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#themeTaxonomy>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Catalog#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ConceptSchema> a modelldcatno:ObjectType ;
    dct:title "ConceptSchema"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#versioninfo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ConceptSchema#versionnumber> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Contact> a modelldcatno:ObjectType ;
    dct:title "Contact"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#email>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#fullname>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#hasTelephone>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#hasURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#organizationName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#organizationUnit>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Contact#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#DataTheme> a modelldcatno:ObjectType ;
    dct:title "DataTheme"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#conceptSchema>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#numberOfHits>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#pickedDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#startUse>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/DataTheme#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#HarvestMetadata> a modelldcatno:ObjectType ;
    dct:title "HarvestMetadata"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#changed>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#firstHarvested>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#lastChanged>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/HarvestMetadata#lastHarvested> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PeriodOfTime> a modelldcatno:ObjectType ;
    dct:title "PeriodOfTime"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PeriodOfTime#startDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Reference> a modelldcatno:ObjectType ;
    dct:title "Reference"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Reference#referenceType>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Reference#source> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Subject> a modelldcatno:ObjectType ;
    dct:title "Subject"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#altLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#creator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#datasets>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#definition>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#inScheme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#note>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#source>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Subject#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Dataset> a modelldcatno:ObjectType ;
    dct:title "Dataset"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accessRights>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accessRightsComment>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#accrualPeriodicity>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#admsIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#catalog>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#conformsTo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#contactPoint>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#descriptionFormatted>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#distribution>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#harvest>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasAccuracyAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasAvailabilityAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasCompletenessAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasCurrentnessAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#hasRelevanceAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#informationModel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#issued>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#keyword>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#landingPage>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#language>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForAccess>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForProcessing>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#legalBasisForRestriction>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#modified>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#objective>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#page>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#provenance>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#provenanceSort>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#references>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#sample>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#source>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#spatial>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#subject>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#temporal>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#theme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Dataset#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Distribution> a modelldcatno:ObjectType ;
    dct:title "Distribution"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#accessURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#conformsTo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#downloadURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#format>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#license>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#openLicense>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#page>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Distribution#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#PublisherHit> a modelldcatno:ObjectType ;
    dct:title "PublisherHit"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#children>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/PublisherHit#orgPath> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Publisher> a modelldcatno:ObjectType ;
    dct:title "Publisher"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#orgPath>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Publisher#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#QualityAnnotation> a modelldcatno:ObjectType ;
    dct:title "QualityAnnotation"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#hasBody>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#inDimension>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/QualityAnnotation#motivatedBy> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosCode> a modelldcatno:ObjectType ;
    dct:title "SkosCode"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosCode#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SkosConcept> a modelldcatno:ObjectType ;
    dct:title "SkosConcept"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#extraType>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SkosConcept#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date-time> a modelldcatno:SimpleType ;
    dct:title "date-time"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
