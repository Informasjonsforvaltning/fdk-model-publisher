"""Example JSON input."""
# flake8: noqa

circular_dependencies_test_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Catalog>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#ConceptSchema>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Contact>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#DataTheme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Dataset>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Distribution>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#HarvestMetadata>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Hits>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PeriodOfTime>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PublisherHit>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Reference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Subject>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Hits> a modelldcatno:ObjectType ;
    dct:title "Hits"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Hits#hits> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#boolean> a modelldcatno:SimpleType ;
    dct:title "boolean"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#dataset> a modelldcatno:Role ;
    dct:title "dataset"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Dataset> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#language> a modelldcatno:Attribute ;
    dct:title "language"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#themeTaxonomy> a modelldcatno:Attribute ;
    dct:title "themeTaxonomy"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#versioninfo> a modelldcatno:Attribute ;
    dct:title "versioninfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#versionnumber> a modelldcatno:Attribute ;
    dct:title "versionnumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#email> a modelldcatno:Attribute ;
    dct:title "email"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#fullname> a modelldcatno:Attribute ;
    dct:title "fullname"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#hasTelephone> a modelldcatno:Attribute ;
    dct:title "hasTelephone"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#hasURL> a modelldcatno:Attribute ;
    dct:title "hasURL"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#organizationName> a modelldcatno:Attribute ;
    dct:title "organizationName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#organizationUnit> a modelldcatno:Attribute ;
    dct:title "organizationUnit"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#conceptSchema> a modelldcatno:Role ;
    dct:title "conceptSchema"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#ConceptSchema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#numberOfHits> a modelldcatno:Attribute ;
    dct:title "numberOfHits"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#pickedDate> a modelldcatno:Attribute ;
    dct:title "pickedDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#startUse> a modelldcatno:Attribute ;
    dct:title "startUse"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accessRights> a modelldcatno:Role ;
    dct:title "accessRights"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accessRightsComment> a modelldcatno:Attribute ;
    dct:title "accessRightsComment"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accrualPeriodicity> a modelldcatno:Role ;
    dct:title "accrualPeriodicity"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#admsIdentifier> a modelldcatno:Attribute ;
    dct:title "admsIdentifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#catalog> a modelldcatno:Role ;
    dct:title "catalog"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Catalog> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#contactPoint> a modelldcatno:Role ;
    dct:title "contactPoint"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Contact> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#descriptionFormatted> a modelldcatno:Attribute ;
    dct:title "descriptionFormatted"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#distribution> a modelldcatno:Role ;
    dct:title "distribution"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Distribution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#harvest> a modelldcatno:Role ;
    dct:title "harvest"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#HarvestMetadata> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasAccuracyAnnotation> a modelldcatno:Role ;
    dct:title "hasAccuracyAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasAvailabilityAnnotation> a modelldcatno:Role ;
    dct:title "hasAvailabilityAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasCompletenessAnnotation> a modelldcatno:Role ;
    dct:title "hasCompletenessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasCurrentnessAnnotation> a modelldcatno:Role ;
    dct:title "hasCurrentnessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasRelevanceAnnotation> a modelldcatno:Role ;
    dct:title "hasRelevanceAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#informationModel> a modelldcatno:Role ;
    dct:title "informationModel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#keyword> a modelldcatno:Attribute ;
    dct:title "keyword"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#landingPage> a modelldcatno:Attribute ;
    dct:title "landingPage"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#language> a modelldcatno:Role ;
    dct:title "language"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForAccess> a modelldcatno:Role ;
    dct:title "legalBasisForAccess"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForProcessing> a modelldcatno:Role ;
    dct:title "legalBasisForProcessing"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForRestriction> a modelldcatno:Role ;
    dct:title "legalBasisForRestriction"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#objective> a modelldcatno:Attribute ;
    dct:title "objective"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#page> a modelldcatno:Attribute ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#provenance> a modelldcatno:Role ;
    dct:title "provenance"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#provenanceSort> a modelldcatno:Attribute ;
    dct:title "provenanceSort"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#references> a modelldcatno:Role ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Reference> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#sample> a modelldcatno:Role ;
    dct:title "sample"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Distribution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#spatial> a modelldcatno:Role ;
    dct:title "spatial"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#subject> a modelldcatno:Role ;
    dct:title "subject"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Subject> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#temporal> a modelldcatno:Role ;
    dct:title "temporal"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PeriodOfTime> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#theme> a modelldcatno:Role ;
    dct:title "theme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#DataTheme> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#accessURL> a modelldcatno:Attribute ;
    dct:title "accessURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#downloadURL> a modelldcatno:Attribute ;
    dct:title "downloadURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#format> a modelldcatno:Attribute ;
    dct:title "format"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#license> a modelldcatno:Role ;
    dct:title "license"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#openLicense> a modelldcatno:Attribute ;
    dct:title "openLicense"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#page> a modelldcatno:Role ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#changed> a modelldcatno:Attribute ;
    dct:title "changed"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#firstHarvested> a modelldcatno:Attribute ;
    dct:title "firstHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#lastChanged> a modelldcatno:Attribute ;
    dct:title "lastChanged"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#lastHarvested> a modelldcatno:Attribute ;
    dct:title "lastHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Hits#hits> a modelldcatno:Role ;
    dct:title "hits"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PublisherHit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#endDate> a modelldcatno:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#startDate> a modelldcatno:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#children> a modelldcatno:Role ;
    dct:title "children"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PublisherHit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#hasBody> a modelldcatno:Attribute ;
    dct:title "hasBody"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#inDimension> a modelldcatno:Attribute ;
    dct:title "inDimension"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#motivatedBy> a modelldcatno:Attribute ;
    dct:title "motivatedBy"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Reference#referenceType> a modelldcatno:Role ;
    dct:title "referenceType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Reference#source> a modelldcatno:Role ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#extraType> a modelldcatno:Attribute ;
    dct:title "extraType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#altLabel> a modelldcatno:Attribute ;
    dct:title "altLabel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#creator> a modelldcatno:Role ;
    dct:title "creator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Publisher> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#datasets> a modelldcatno:Role ;
    dct:title "datasets"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Dataset> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#definition> a modelldcatno:Attribute ;
    dct:title "definition"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#inScheme> a modelldcatno:Attribute ;
    dct:title "inScheme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#note> a modelldcatno:Attribute ;
    dct:title "note"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Catalog> a modelldcatno:ObjectType ;
    dct:title "Catalog"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#dataset>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#issued>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#language>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#modified>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#themeTaxonomy>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Catalog#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#ConceptSchema> a modelldcatno:ObjectType ;
    dct:title "ConceptSchema"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#versioninfo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/ConceptSchema#versionnumber> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Contact> a modelldcatno:ObjectType ;
    dct:title "Contact"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#email>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#fullname>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#hasTelephone>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#hasURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#organizationName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#organizationUnit>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Contact#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#DataTheme> a modelldcatno:ObjectType ;
    dct:title "DataTheme"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#conceptSchema>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#numberOfHits>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#pickedDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#startUse>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/DataTheme#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#HarvestMetadata> a modelldcatno:ObjectType ;
    dct:title "HarvestMetadata"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#changed>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#firstHarvested>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#lastChanged>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/HarvestMetadata#lastHarvested> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PeriodOfTime> a modelldcatno:ObjectType ;
    dct:title "PeriodOfTime"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PeriodOfTime#startDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Reference> a modelldcatno:ObjectType ;
    dct:title "Reference"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Reference#referenceType>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Reference#source> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Subject> a modelldcatno:ObjectType ;
    dct:title "Subject"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#altLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#creator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#datasets>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#definition>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#inScheme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#note>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#source>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Subject#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Dataset> a modelldcatno:ObjectType ;
    dct:title "Dataset"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accessRights>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accessRightsComment>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#accrualPeriodicity>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#admsIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#catalog>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#conformsTo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#contactPoint>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#descriptionFormatted>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#distribution>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#harvest>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasAccuracyAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasAvailabilityAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasCompletenessAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasCurrentnessAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#hasRelevanceAnnotation>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#informationModel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#issued>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#keyword>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#landingPage>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#language>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForAccess>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForProcessing>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#legalBasisForRestriction>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#modified>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#objective>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#page>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#provenance>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#provenanceSort>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#publisher>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#references>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#sample>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#source>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#spatial>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#subject>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#temporal>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#theme>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Dataset#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Distribution> a modelldcatno:ObjectType ;
    dct:title "Distribution"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#accessURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#conformsTo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#description>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#downloadURL>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#format>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#license>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#openLicense>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#page>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#title>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Distribution#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#PublisherHit> a modelldcatno:ObjectType ;
    dct:title "PublisherHit"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#children>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/PublisherHit#orgPath> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#Publisher> a modelldcatno:ObjectType ;
    dct:title "Publisher"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#orgPath>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/Publisher#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#QualityAnnotation> a modelldcatno:ObjectType ;
    dct:title "QualityAnnotation"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#hasBody>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#inDimension>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/QualityAnnotation#motivatedBy> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosCode> a modelldcatno:ObjectType ;
    dct:title "SkosCode"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosCode#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#SkosConcept> a modelldcatno:ObjectType ;
    dct:title "SkosConcept"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#extraType>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#prefLabel>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5/SkosConcept#uri> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#date-time> a modelldcatno:SimpleType ;
    dct:title "date-time"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/e3a031fe644565af181e1049ab3e99754ddc60d5#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
