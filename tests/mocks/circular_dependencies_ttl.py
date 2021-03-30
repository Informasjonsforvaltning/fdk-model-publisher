"""Example JSON input."""
# flake8: noqa

circular_dependencies_test_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Catalog>,
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
        <http://uri.com#String>,
        <http://uri.com#Subject> .

<http://uri.com#Boolean> a ns1:SimpleType ;
    dct:title "Boolean"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<http://uri.com#Hits> a ns1:ObjectType ;
    dct:title "Hits"@en ;
    ns1:hasProperty <http://uri.com/Hits#hits> .

<http://uri.com#Int32> a ns1:SimpleType ;
    dct:title "Int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com/Catalog#dataset> a ns1:Role ;
    dct:title "dataset"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Dataset> .

<http://uri.com/Catalog#description> a ns1:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Catalog#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Catalog#issued> a ns1:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Catalog#language> a ns1:Attribute ;
    dct:title "language"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Catalog#modified> a ns1:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Catalog#publisher> a ns1:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Catalog#themeTaxonomy> a ns1:Attribute ;
    dct:title "themeTaxonomy"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Catalog#title> a ns1:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Catalog#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/ConceptSchema#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/ConceptSchema#title> a ns1:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/ConceptSchema#versioninfo> a ns1:Attribute ;
    dct:title "versioninfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/ConceptSchema#versionnumber> a ns1:Attribute ;
    dct:title "versionnumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#email> a ns1:Attribute ;
    dct:title "email"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#fullname> a ns1:Attribute ;
    dct:title "fullname"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#hasTelephone> a ns1:Attribute ;
    dct:title "hasTelephone"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#hasURL> a ns1:Attribute ;
    dct:title "hasURL"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#organizationName> a ns1:Attribute ;
    dct:title "organizationName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#organizationUnit> a ns1:Attribute ;
    dct:title "organizationUnit"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Contact#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#conceptSchema> a ns1:Role ;
    dct:title "conceptSchema"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#ConceptSchema> .

<http://uri.com/DataTheme#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#numberOfHits> a ns1:Attribute ;
    dct:title "numberOfHits"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/DataTheme#pickedDate> a ns1:Attribute ;
    dct:title "pickedDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#startUse> a ns1:Attribute ;
    dct:title "startUse"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#title> a ns1:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/DataTheme#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#accessRights> a ns1:Role ;
    dct:title "accessRights"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#accessRightsComment> a ns1:Attribute ;
    dct:title "accessRightsComment"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#accrualPeriodicity> a ns1:Role ;
    dct:title "accrualPeriodicity"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#admsIdentifier> a ns1:Attribute ;
    dct:title "admsIdentifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#catalog> a ns1:Role ;
    dct:title "catalog"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Catalog> .

<http://uri.com/Dataset#conformsTo> a ns1:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#contactPoint> a ns1:Role ;
    dct:title "contactPoint"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Contact> .

<http://uri.com/Dataset#description> a ns1:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#descriptionFormatted> a ns1:Attribute ;
    dct:title "descriptionFormatted"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#distribution> a ns1:Role ;
    dct:title "distribution"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Distribution> .

<http://uri.com/Dataset#harvest> a ns1:Role ;
    dct:title "harvest"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#HarvestMetadata> .

<http://uri.com/Dataset#hasAccuracyAnnotation> a ns1:Role ;
    dct:title "hasAccuracyAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasAvailabilityAnnotation> a ns1:Role ;
    dct:title "hasAvailabilityAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasCompletenessAnnotation> a ns1:Role ;
    dct:title "hasCompletenessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasCurrentnessAnnotation> a ns1:Role ;
    dct:title "hasCurrentnessAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#hasRelevanceAnnotation> a ns1:Role ;
    dct:title "hasRelevanceAnnotation"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#QualityAnnotation> .

<http://uri.com/Dataset#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#identifier> a ns1:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#informationModel> a ns1:Role ;
    dct:title "informationModel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#issued> a ns1:Attribute ;
    dct:title "issued"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Dataset#keyword> a ns1:Attribute ;
    dct:title "keyword"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#landingPage> a ns1:Attribute ;
    dct:title "landingPage"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#language> a ns1:Role ;
    dct:title "language"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#legalBasisForAccess> a ns1:Role ;
    dct:title "legalBasisForAccess"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#legalBasisForProcessing> a ns1:Role ;
    dct:title "legalBasisForProcessing"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#legalBasisForRestriction> a ns1:Role ;
    dct:title "legalBasisForRestriction"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Dataset#modified> a ns1:Attribute ;
    dct:title "modified"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Dataset#objective> a ns1:Attribute ;
    dct:title "objective"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#page> a ns1:Attribute ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#provenance> a ns1:Role ;
    dct:title "provenance"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#provenanceSort> a ns1:Attribute ;
    dct:title "provenanceSort"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#publisher> a ns1:Role ;
    dct:title "publisher"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Dataset#references> a ns1:Role ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Reference> .

<http://uri.com/Dataset#sample> a ns1:Role ;
    dct:title "sample"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Distribution> .

<http://uri.com/Dataset#source> a ns1:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#spatial> a ns1:Role ;
    dct:title "spatial"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Dataset#subject> a ns1:Role ;
    dct:title "subject"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Subject> .

<http://uri.com/Dataset#temporal> a ns1:Role ;
    dct:title "temporal"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#PeriodOfTime> .

<http://uri.com/Dataset#theme> a ns1:Role ;
    dct:title "theme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#DataTheme> .

<http://uri.com/Dataset#title> a ns1:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Dataset#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#accessURL> a ns1:Attribute ;
    dct:title "accessURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#conformsTo> a ns1:Role ;
    dct:title "conformsTo"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#description> a ns1:Attribute ;
    dct:title "description"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#downloadURL> a ns1:Attribute ;
    dct:title "downloadURL"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#format> a ns1:Attribute ;
    dct:title "format"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#license> a ns1:Role ;
    dct:title "license"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#openLicense> a ns1:Attribute ;
    dct:title "openLicense"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Boolean> .

<http://uri.com/Distribution#page> a ns1:Role ;
    dct:title "page"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/Distribution#title> a ns1:Attribute ;
    dct:title "title"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Distribution#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/HarvestMetadata#changed> a ns1:Attribute ;
    dct:title "changed"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/HarvestMetadata#firstHarvested> a ns1:Attribute ;
    dct:title "firstHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/HarvestMetadata#lastChanged> a ns1:Attribute ;
    dct:title "lastChanged"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/HarvestMetadata#lastHarvested> a ns1:Attribute ;
    dct:title "lastHarvested"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Hits#hits> a ns1:Role ;
    dct:title "hits"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#PublisherHit> .

<http://uri.com/PeriodOfTime#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/PeriodOfTime#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/PeriodOfTime#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/PeriodOfTime#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Date-time> .

<http://uri.com/Publisher#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Publisher#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Publisher#orgPath> a ns1:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Publisher#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/PublisherHit#children> a ns1:Role ;
    dct:title "children"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#PublisherHit> .

<http://uri.com/PublisherHit#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/PublisherHit#orgPath> a ns1:Attribute ;
    dct:title "orgPath"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/QualityAnnotation#hasBody> a ns1:Attribute ;
    dct:title "hasBody"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/QualityAnnotation#inDimension> a ns1:Attribute ;
    dct:title "inDimension"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/QualityAnnotation#motivatedBy> a ns1:Attribute ;
    dct:title "motivatedBy"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Reference#referenceType> a ns1:Role ;
    dct:title "referenceType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosCode> .

<http://uri.com/Reference#source> a ns1:Role ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#SkosConcept> .

<http://uri.com/SkosCode#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SkosCode#prefLabel> a ns1:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SkosCode#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SkosConcept#extraType> a ns1:Attribute ;
    dct:title "extraType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SkosConcept#prefLabel> a ns1:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SkosConcept#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#altLabel> a ns1:Attribute ;
    dct:title "altLabel"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#creator> a ns1:Role ;
    dct:title "creator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Publisher> .

<http://uri.com/Subject#datasets> a ns1:Role ;
    dct:title "datasets"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Dataset> .

<http://uri.com/Subject#definition> a ns1:Attribute ;
    dct:title "definition"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#identifier> a ns1:Attribute ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#inScheme> a ns1:Attribute ;
    dct:title "inScheme"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#note> a ns1:Attribute ;
    dct:title "note"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#prefLabel> a ns1:Attribute ;
    dct:title "prefLabel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#source> a ns1:Attribute ;
    dct:title "source"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Subject#uri> a ns1:Attribute ;
    dct:title "uri"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#Catalog> a ns1:ObjectType ;
    dct:title "Catalog"@en ;
    ns1:hasProperty <http://uri.com/Catalog#dataset>,
        <http://uri.com/Catalog#description>,
        <http://uri.com/Catalog#id>,
        <http://uri.com/Catalog#issued>,
        <http://uri.com/Catalog#language>,
        <http://uri.com/Catalog#modified>,
        <http://uri.com/Catalog#publisher>,
        <http://uri.com/Catalog#themeTaxonomy>,
        <http://uri.com/Catalog#title>,
        <http://uri.com/Catalog#uri> .

<http://uri.com#ConceptSchema> a ns1:ObjectType ;
    dct:title "ConceptSchema"@en ;
    ns1:hasProperty <http://uri.com/ConceptSchema#id>,
        <http://uri.com/ConceptSchema#title>,
        <http://uri.com/ConceptSchema#versioninfo>,
        <http://uri.com/ConceptSchema#versionnumber> .

<http://uri.com#Contact> a ns1:ObjectType ;
    dct:title "Contact"@en ;
    ns1:hasProperty <http://uri.com/Contact#email>,
        <http://uri.com/Contact#fullname>,
        <http://uri.com/Contact#hasTelephone>,
        <http://uri.com/Contact#hasURL>,
        <http://uri.com/Contact#id>,
        <http://uri.com/Contact#organizationName>,
        <http://uri.com/Contact#organizationUnit>,
        <http://uri.com/Contact#uri> .

<http://uri.com#DataTheme> a ns1:ObjectType ;
    dct:title "DataTheme"@en ;
    ns1:hasProperty <http://uri.com/DataTheme#code>,
        <http://uri.com/DataTheme#conceptSchema>,
        <http://uri.com/DataTheme#id>,
        <http://uri.com/DataTheme#numberOfHits>,
        <http://uri.com/DataTheme#pickedDate>,
        <http://uri.com/DataTheme#startUse>,
        <http://uri.com/DataTheme#title>,
        <http://uri.com/DataTheme#uri> .

<http://uri.com#HarvestMetadata> a ns1:ObjectType ;
    dct:title "HarvestMetadata"@en ;
    ns1:hasProperty <http://uri.com/HarvestMetadata#changed>,
        <http://uri.com/HarvestMetadata#firstHarvested>,
        <http://uri.com/HarvestMetadata#lastChanged>,
        <http://uri.com/HarvestMetadata#lastHarvested> .

<http://uri.com#PeriodOfTime> a ns1:ObjectType ;
    dct:title "PeriodOfTime"@en ;
    ns1:hasProperty <http://uri.com/PeriodOfTime#endDate>,
        <http://uri.com/PeriodOfTime#id>,
        <http://uri.com/PeriodOfTime#name>,
        <http://uri.com/PeriodOfTime#startDate> .

<http://uri.com#Reference> a ns1:ObjectType ;
    dct:title "Reference"@en ;
    ns1:hasProperty <http://uri.com/Reference#referenceType>,
        <http://uri.com/Reference#source> .

<http://uri.com#Subject> a ns1:ObjectType ;
    dct:title "Subject"@en ;
    ns1:hasProperty <http://uri.com/Subject#altLabel>,
        <http://uri.com/Subject#creator>,
        <http://uri.com/Subject#datasets>,
        <http://uri.com/Subject#definition>,
        <http://uri.com/Subject#identifier>,
        <http://uri.com/Subject#inScheme>,
        <http://uri.com/Subject#note>,
        <http://uri.com/Subject#prefLabel>,
        <http://uri.com/Subject#source>,
        <http://uri.com/Subject#uri> .

<http://uri.com#Dataset> a ns1:ObjectType ;
    dct:title "Dataset"@en ;
    ns1:hasProperty <http://uri.com/Dataset#accessRights>,
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

<http://uri.com#Distribution> a ns1:ObjectType ;
    dct:title "Distribution"@en ;
    ns1:hasProperty <http://uri.com/Distribution#accessURL>,
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

<http://uri.com#PublisherHit> a ns1:ObjectType ;
    dct:title "PublisherHit"@en ;
    ns1:hasProperty <http://uri.com/PublisherHit#children>,
        <http://uri.com/PublisherHit#name>,
        <http://uri.com/PublisherHit#orgPath> .

<http://uri.com#Publisher> a ns1:ObjectType ;
    dct:title "Publisher"@en ;
    ns1:hasProperty <http://uri.com/Publisher#id>,
        <http://uri.com/Publisher#name>,
        <http://uri.com/Publisher#orgPath>,
        <http://uri.com/Publisher#uri> .

<http://uri.com#QualityAnnotation> a ns1:ObjectType ;
    dct:title "QualityAnnotation"@en ;
    ns1:hasProperty <http://uri.com/QualityAnnotation#hasBody>,
        <http://uri.com/QualityAnnotation#inDimension>,
        <http://uri.com/QualityAnnotation#motivatedBy> .

<http://uri.com#SkosCode> a ns1:ObjectType ;
    dct:title "SkosCode"@en ;
    ns1:hasProperty <http://uri.com/SkosCode#code>,
        <http://uri.com/SkosCode#prefLabel>,
        <http://uri.com/SkosCode#uri> .

<http://uri.com#Date-time> a ns1:SimpleType ;
    dct:title "Date-time"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#SkosConcept> a ns1:ObjectType ;
    dct:title "SkosConcept"@en ;
    ns1:hasProperty <http://uri.com/SkosConcept#extraType>,
        <http://uri.com/SkosConcept#prefLabel>,
        <http://uri.com/SkosConcept#uri> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .


"""
