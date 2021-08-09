"""Example JSON input."""
# flake8: noqa

circular_dependencies_test_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Catalog>,
        <http://uri.com#ConceptSchema>,
        <http://uri.com#Contact>,
        <http://uri.com#DataTheme>,
        <http://uri.com#Dataset>,
        <http://uri.com#Distribution>,
        <http://uri.com#HarvestMetadata>,
        <http://uri.com#Hits>,
        <http://uri.com#PeriodOfTime>,
        <http://uri.com#Publisher>,
        <http://uri.com#PublisherHit>,
        <http://uri.com#QualityAnnotation>,
        <http://uri.com#Reference>,
        <http://uri.com#SkosCode>,
        <http://uri.com#SkosConcept>,
        <http://uri.com#Subject>,
        <http://uri.com#string> .

<http://uri.com#Hits> a modelldcatno:ObjectType ;
    dct:title "Hits"@en ;
    modelldcatno:hasProperty <http://uri.com/Hits#hits> .

<http://uri.com#boolean> a modelldcatno:SimpleType ;
    dct:title "boolean"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<http://uri.com#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Catalog#dataset> a modelldcatno:Role ;
    dct:title "dataset"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Dataset> .

<http://uri.com/Catalog#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Catalog#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Catalog#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Catalog#language> a modelldcatno:Attribute ;
    dct:title "language"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Catalog#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Catalog#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Catalog#themeTaxonomy> a modelldcatno:Attribute ;
    dct:title "themeTaxonomy"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Catalog#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Catalog#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/ConceptSchema#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/ConceptSchema#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/ConceptSchema#versioninfo> a modelldcatno:Attribute ;
    dct:title "versioninfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/ConceptSchema#versionnumber> a modelldcatno:Attribute ;
    dct:title "versionnumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#email> a modelldcatno:Attribute ;
    dct:title "email"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#fullname> a modelldcatno:Attribute ;
    dct:title "fullname"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#hasTelephone> a modelldcatno:Attribute ;
    dct:title "hasTelephone"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#hasURL> a modelldcatno:Attribute ;
    dct:title "hasURL"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#organizationName> a modelldcatno:Attribute ;
    dct:title "organizationName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#organizationUnit> a modelldcatno:Attribute ;
    dct:title "organizationUnit"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Contact#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#conceptSchema> a modelldcatno:Role ;
    dct:title "conceptSchema"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#ConceptSchema> .

<http://uri.com/DataTheme#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#numberOfHits> a modelldcatno:Attribute ;
    dct:title "numberOfHits"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/DataTheme#pickedDate> a modelldcatno:Attribute ;
    dct:title "pickedDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#startUse> a modelldcatno:Attribute ;
    dct:title "startUse"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/DataTheme#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#accessRights> a modelldcatno:Role ;
    dct:title "accessRights"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#accessRightsComment> a modelldcatno:Attribute ;
    dct:title "accessRightsComment"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#accrualPeriodicity> a modelldcatno:Role ;
    dct:title "accrualPeriodicity"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#admsIdentifier> a modelldcatno:Attribute ;
    dct:title "admsIdentifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#catalog> a modelldcatno:Role ;
    dct:title "catalog"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Catalog> .

<http://uri.com/Dataset#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#contactPoint> a modelldcatno:Role ;
    dct:title "contactPoint"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Contact> .

<http://uri.com/Dataset#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#descriptionFormatted> a modelldcatno:Attribute ;
    dct:title "descriptionFormatted"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#distribution> a modelldcatno:Role ;
    dct:title "distribution"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Distribution> .

<http://uri.com/Dataset#harvest> a modelldcatno:Role ;
    dct:title "harvest"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#HarvestMetadata> .

<http://uri.com/Dataset#hasAccuracyAnnotation> a modelldcatno:Role ;
    dct:title "hasAccuracyAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasAvailabilityAnnotation> a modelldcatno:Role ;
    dct:title "hasAvailabilityAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasCompletenessAnnotation> a modelldcatno:Role ;
    dct:title "hasCompletenessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasCurrentnessAnnotation> a modelldcatno:Role ;
    dct:title "hasCurrentnessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasRelevanceAnnotation> a modelldcatno:Role ;
    dct:title "hasRelevanceAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#informationModel> a modelldcatno:Role ;
    dct:title "informationModel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#issued> a modelldcatno:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Dataset#keyword> a modelldcatno:Attribute ;
    dct:title "keyword"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#landingPage> a modelldcatno:Attribute ;
    dct:title "landingPage"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#language> a modelldcatno:Role ;
    dct:title "language"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#legalBasisForAccess> a modelldcatno:Role ;
    dct:title "legalBasisForAccess"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#legalBasisForProcessing> a modelldcatno:Role ;
    dct:title "legalBasisForProcessing"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#legalBasisForRestriction> a modelldcatno:Role ;
    dct:title "legalBasisForRestriction"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#modified> a modelldcatno:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Dataset#objective> a modelldcatno:Attribute ;
    dct:title "objective"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#page> a modelldcatno:Attribute ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#provenance> a modelldcatno:Role ;
    dct:title "provenance"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#provenanceSort> a modelldcatno:Attribute ;
    dct:title "provenanceSort"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#publisher> a modelldcatno:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Dataset#references> a modelldcatno:Role ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Reference> .

<http://uri.com/Dataset#sample> a modelldcatno:Role ;
    dct:title "sample"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Distribution> .

<http://uri.com/Dataset#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#spatial> a modelldcatno:Role ;
    dct:title "spatial"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#subject> a modelldcatno:Role ;
    dct:title "subject"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Subject> .

<http://uri.com/Dataset#temporal> a modelldcatno:Role ;
    dct:title "temporal"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#PeriodOfTime> .

<http://uri.com/Dataset#theme> a modelldcatno:Role ;
    dct:title "theme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#DataTheme> .

<http://uri.com/Dataset#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Dataset#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#accessURL> a modelldcatno:Attribute ;
    dct:title "accessURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#conformsTo> a modelldcatno:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#description> a modelldcatno:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#downloadURL> a modelldcatno:Attribute ;
    dct:title "downloadURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#format> a modelldcatno:Attribute ;
    dct:title "format"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#license> a modelldcatno:Role ;
    dct:title "license"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#openLicense> a modelldcatno:Attribute ;
    dct:title "openLicense"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#boolean> .

<http://uri.com/Distribution#page> a modelldcatno:Role ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#title> a modelldcatno:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Distribution#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/HarvestMetadata#changed> a modelldcatno:Attribute ;
    dct:title "changed"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/HarvestMetadata#firstHarvested> a modelldcatno:Attribute ;
    dct:title "firstHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/HarvestMetadata#lastChanged> a modelldcatno:Attribute ;
    dct:title "lastChanged"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/HarvestMetadata#lastHarvested> a modelldcatno:Attribute ;
    dct:title "lastHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Hits#hits> a modelldcatno:Role ;
    dct:title "hits"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#PublisherHit> .

<http://uri.com/PeriodOfTime#endDate> a modelldcatno:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/PeriodOfTime#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/PeriodOfTime#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/PeriodOfTime#startDate> a modelldcatno:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date-time> .

<http://uri.com/Publisher#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Publisher#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Publisher#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Publisher#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/PublisherHit#children> a modelldcatno:Role ;
    dct:title "children"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#PublisherHit> .

<http://uri.com/PublisherHit#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/PublisherHit#orgPath> a modelldcatno:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/QualityAnnotation#hasBody> a modelldcatno:Attribute ;
    dct:title "hasBody"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/QualityAnnotation#inDimension> a modelldcatno:Attribute ;
    dct:title "inDimension"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/QualityAnnotation#motivatedBy> a modelldcatno:Attribute ;
    dct:title "motivatedBy"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Reference#referenceType> a modelldcatno:Role ;
    dct:title "referenceType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Reference#source> a modelldcatno:Role ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/SkosCode#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SkosCode#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SkosCode#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SkosConcept#extraType> a modelldcatno:Attribute ;
    dct:title "extraType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SkosConcept#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SkosConcept#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#altLabel> a modelldcatno:Attribute ;
    dct:title "altLabel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#creator> a modelldcatno:Role ;
    dct:title "creator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Subject#datasets> a modelldcatno:Role ;
    dct:title "datasets"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Dataset> .

<http://uri.com/Subject#definition> a modelldcatno:Attribute ;
    dct:title "definition"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#identifier> a modelldcatno:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#inScheme> a modelldcatno:Attribute ;
    dct:title "inScheme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#note> a modelldcatno:Attribute ;
    dct:title "note"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#prefLabel> a modelldcatno:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#source> a modelldcatno:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Subject#uri> a modelldcatno:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#Catalog> a modelldcatno:ObjectType ;
    dct:title "Catalog"@en ;
    modelldcatno:hasProperty <http://uri.com/Catalog#dataset>,
        <http://uri.com/Catalog#description>,
        <http://uri.com/Catalog#id>,
        <http://uri.com/Catalog#issued>,
        <http://uri.com/Catalog#language>,
        <http://uri.com/Catalog#modified>,
        <http://uri.com/Catalog#publisher>,
        <http://uri.com/Catalog#themeTaxonomy>,
        <http://uri.com/Catalog#title>,
        <http://uri.com/Catalog#uri> .

<http://uri.com#ConceptSchema> a modelldcatno:ObjectType ;
    dct:title "ConceptSchema"@en ;
    modelldcatno:hasProperty <http://uri.com/ConceptSchema#id>,
        <http://uri.com/ConceptSchema#title>,
        <http://uri.com/ConceptSchema#versioninfo>,
        <http://uri.com/ConceptSchema#versionnumber> .

<http://uri.com#Contact> a modelldcatno:ObjectType ;
    dct:title "Contact"@en ;
    modelldcatno:hasProperty <http://uri.com/Contact#email>,
        <http://uri.com/Contact#fullname>,
        <http://uri.com/Contact#hasTelephone>,
        <http://uri.com/Contact#hasURL>,
        <http://uri.com/Contact#id>,
        <http://uri.com/Contact#organizationName>,
        <http://uri.com/Contact#organizationUnit>,
        <http://uri.com/Contact#uri> .

<http://uri.com#DataTheme> a modelldcatno:ObjectType ;
    dct:title "DataTheme"@en ;
    modelldcatno:hasProperty <http://uri.com/DataTheme#code>,
        <http://uri.com/DataTheme#conceptSchema>,
        <http://uri.com/DataTheme#id>,
        <http://uri.com/DataTheme#numberOfHits>,
        <http://uri.com/DataTheme#pickedDate>,
        <http://uri.com/DataTheme#startUse>,
        <http://uri.com/DataTheme#title>,
        <http://uri.com/DataTheme#uri> .

<http://uri.com#HarvestMetadata> a modelldcatno:ObjectType ;
    dct:title "HarvestMetadata"@en ;
    modelldcatno:hasProperty <http://uri.com/HarvestMetadata#changed>,
        <http://uri.com/HarvestMetadata#firstHarvested>,
        <http://uri.com/HarvestMetadata#lastChanged>,
        <http://uri.com/HarvestMetadata#lastHarvested> .

<http://uri.com#PeriodOfTime> a modelldcatno:ObjectType ;
    dct:title "PeriodOfTime"@en ;
    modelldcatno:hasProperty <http://uri.com/PeriodOfTime#endDate>,
        <http://uri.com/PeriodOfTime#id>,
        <http://uri.com/PeriodOfTime#name>,
        <http://uri.com/PeriodOfTime#startDate> .

<http://uri.com#Reference> a modelldcatno:ObjectType ;
    dct:title "Reference"@en ;
    modelldcatno:hasProperty <http://uri.com/Reference#referenceType>,
        <http://uri.com/Reference#source> .

<http://uri.com#Subject> a modelldcatno:ObjectType ;
    dct:title "Subject"@en ;
    modelldcatno:hasProperty <http://uri.com/Subject#altLabel>,
        <http://uri.com/Subject#creator>,
        <http://uri.com/Subject#datasets>,
        <http://uri.com/Subject#definition>,
        <http://uri.com/Subject#identifier>,
        <http://uri.com/Subject#inScheme>,
        <http://uri.com/Subject#note>,
        <http://uri.com/Subject#prefLabel>,
        <http://uri.com/Subject#source>,
        <http://uri.com/Subject#uri> .

<http://uri.com#Dataset> a modelldcatno:ObjectType ;
    dct:title "Dataset"@en ;
    modelldcatno:hasProperty <http://uri.com/Dataset#accessRights>,
        <http://uri.com/Dataset#accessRightsComment>,
        <http://uri.com/Dataset#accrualPeriodicity>,
        <http://uri.com/Dataset#admsIdentifier>,
        <http://uri.com/Dataset#catalog>,
        <http://uri.com/Dataset#conformsTo>,
        <http://uri.com/Dataset#contactPoint>,
        <http://uri.com/Dataset#description>,
        <http://uri.com/Dataset#descriptionFormatted>,
        <http://uri.com/Dataset#distribution>,
        <http://uri.com/Dataset#harvest>,
        <http://uri.com/Dataset#hasAccuracyAnnotation>,
        <http://uri.com/Dataset#hasAvailabilityAnnotation>,
        <http://uri.com/Dataset#hasCompletenessAnnotation>,
        <http://uri.com/Dataset#hasCurrentnessAnnotation>,
        <http://uri.com/Dataset#hasRelevanceAnnotation>,
        <http://uri.com/Dataset#id>,
        <http://uri.com/Dataset#identifier>,
        <http://uri.com/Dataset#informationModel>,
        <http://uri.com/Dataset#issued>,
        <http://uri.com/Dataset#keyword>,
        <http://uri.com/Dataset#landingPage>,
        <http://uri.com/Dataset#language>,
        <http://uri.com/Dataset#legalBasisForAccess>,
        <http://uri.com/Dataset#legalBasisForProcessing>,
        <http://uri.com/Dataset#legalBasisForRestriction>,
        <http://uri.com/Dataset#modified>,
        <http://uri.com/Dataset#objective>,
        <http://uri.com/Dataset#page>,
        <http://uri.com/Dataset#provenance>,
        <http://uri.com/Dataset#provenanceSort>,
        <http://uri.com/Dataset#publisher>,
        <http://uri.com/Dataset#references>,
        <http://uri.com/Dataset#sample>,
        <http://uri.com/Dataset#source>,
        <http://uri.com/Dataset#spatial>,
        <http://uri.com/Dataset#subject>,
        <http://uri.com/Dataset#temporal>,
        <http://uri.com/Dataset#theme>,
        <http://uri.com/Dataset#title>,
        <http://uri.com/Dataset#type>,
        <http://uri.com/Dataset#uri> .

<http://uri.com#Distribution> a modelldcatno:ObjectType ;
    dct:title "Distribution"@en ;
    modelldcatno:hasProperty <http://uri.com/Distribution#accessURL>,
        <http://uri.com/Distribution#conformsTo>,
        <http://uri.com/Distribution#description>,
        <http://uri.com/Distribution#downloadURL>,
        <http://uri.com/Distribution#format>,
        <http://uri.com/Distribution#id>,
        <http://uri.com/Distribution#license>,
        <http://uri.com/Distribution#openLicense>,
        <http://uri.com/Distribution#page>,
        <http://uri.com/Distribution#title>,
        <http://uri.com/Distribution#type>,
        <http://uri.com/Distribution#uri> .

<http://uri.com#PublisherHit> a modelldcatno:ObjectType ;
    dct:title "PublisherHit"@en ;
    modelldcatno:hasProperty <http://uri.com/PublisherHit#children>,
        <http://uri.com/PublisherHit#name>,
        <http://uri.com/PublisherHit#orgPath> .

<http://uri.com#Publisher> a modelldcatno:ObjectType ;
    dct:title "Publisher"@en ;
    modelldcatno:hasProperty <http://uri.com/Publisher#id>,
        <http://uri.com/Publisher#name>,
        <http://uri.com/Publisher#orgPath>,
        <http://uri.com/Publisher#uri> .

<http://uri.com#QualityAnnotation> a modelldcatno:ObjectType ;
    dct:title "QualityAnnotation"@en ;
    modelldcatno:hasProperty <http://uri.com/QualityAnnotation#hasBody>,
        <http://uri.com/QualityAnnotation#inDimension>,
        <http://uri.com/QualityAnnotation#motivatedBy> .

<http://uri.com#SkosCode> a modelldcatno:ObjectType ;
    dct:title "SkosCode"@en ;
    modelldcatno:hasProperty <http://uri.com/SkosCode#code>,
        <http://uri.com/SkosCode#prefLabel>,
        <http://uri.com/SkosCode#uri> .

<http://uri.com#SkosConcept> a modelldcatno:ObjectType ;
    dct:title "SkosConcept"@en ;
    modelldcatno:hasProperty <http://uri.com/SkosConcept#extraType>,
        <http://uri.com/SkosConcept#prefLabel>,
        <http://uri.com/SkosConcept#uri> .

<http://uri.com#date-time> a modelldcatno:SimpleType ;
    dct:title "date-time"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
