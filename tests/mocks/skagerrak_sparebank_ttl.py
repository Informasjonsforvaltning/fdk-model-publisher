"""Example TTL output."""
skagerrak_sparebank_ttl_mock = """
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://fdk-model-publisher.fellesdatakatalog.no> a dcat:Catalog ;
    dct:title "FDK informasjonsmodellkatalog"@nb ;
    ns1:model <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> .

<https://fdk-model-publisher.fellesdatakatalog.no#937891245> a foaf:Agent ;
    dct:identifier "937891245" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> a ns1:InformationModel ;
    dct:conformsTo <https://data.norge.no/specification/kontoopplysninger> ;
    dct:description "Open API specification of the Account APIs. (Work in progress.)"@en ;
    dct:publisher <https://fdk-model-publisher.fellesdatakatalog.no#937891245> ;
    dct:title "Information Model - Accounts API Skagerrak Sparebank"@en ;
    ns1:containsModelelement <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error400>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error401>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error403>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error404>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error405>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error429>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error500>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODateTime>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> a ns1:ObjectType ;
    dct:title "Account"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> a ns1:ObjectType ;
    dct:title "AccountDetail"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails> a ns1:ObjectType ;
    dct:title "AccountDetails"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber> a ns1:Attribute ;
    dct:title "AccountNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> a ns1:Attribute ;
    dct:title "AccountPermissionType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference> a ns1:Attribute ;
    dct:title "AccountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> a ns1:ObjectType ;
    dct:title "AccountRole"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> a ns1:Attribute ;
    dct:title "AccountStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> a ns1:Attribute ;
    dct:title "AccountType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts> a ns1:ObjectType ;
    dct:title "Accounts"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> a ns1:Attribute ;
    dct:title "AddressType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> a ns1:Attribute ;
    dct:title "Amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> a ns1:ObjectType ;
    dct:title "Balance"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> a ns1:Attribute ;
    dct:title "BalanceType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> a ns1:ObjectType ;
    dct:title "BankTransactionCode"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#freeText> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardNumber> a ns1:Attribute ;
    dct:title "CardNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> a ns1:Attribute ;
    dct:title "CardType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards> a ns1:ObjectType ;
    dct:title "Cards"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty> a ns1:ObjectType ;
    dct:title "CounterParty"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> a ns1:Attribute ;
    dct:title "CounterPartyType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> a ns1:Attribute ;
    dct:title "CountryCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> a ns1:Attribute ;
    dct:title "CreditOrDebit"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> a ns1:Attribute ;
    dct:title "CurrencyCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> a ns1:ObjectType ;
    dct:title "CurrencyExchange"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> a ns1:Attribute ;
    dct:title "DomainType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> a ns1:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> a ns1:Attribute ;
    dct:title "ElectronicAddressType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error> a ns1:ObjectType ;
    dct:title "Error"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error400> a ns1:ObjectType ;
    dct:title "Error400"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error401> a ns1:ObjectType ;
    dct:title "Error401"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error403> a ns1:ObjectType ;
    dct:title "Error403"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error404> a ns1:ObjectType ;
    dct:title "Error404"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error405> a ns1:ObjectType ;
    dct:title "Error405"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error429> a ns1:ObjectType ;
    dct:title "Error429"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error500> a ns1:ObjectType ;
    dct:title "Error500"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> a ns1:Attribute ;
    dct:title "FamilyType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> a ns1:ObjectType ;
    dct:title "FinancialInstitution"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate> a ns1:Attribute ;
    dct:title "ISODate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODateTime> a ns1:Attribute ;
    dct:title "ISODateTime"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth> a ns1:Attribute ;
    dct:title "ISOYearMonth"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> a ns1:ObjectType ;
    dct:title "Identifier"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> a ns1:Attribute ;
    dct:title "IdentifierType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> a ns1:ObjectType ;
    dct:title "Link"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#href>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rel> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> a ns1:ObjectType ;
    dct:title "PaymentCard"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cardIssuerName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#holderName> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> a ns1:ObjectType ;
    dct:title "PostalAddress"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> a ns1:Attribute ;
    dct:title "ResponseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles> a ns1:ObjectType ;
    dct:title "Roles"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> a ns1:Attribute ;
    dct:title "SubFamilyType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction> a ns1:ObjectType ;
    dct:title "Transaction"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalInfo>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#merchant>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#transactionIdentifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference> a ns1:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> a ns1:Attribute ;
    dct:title "TransactionReferenceType"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> a ns1:Attribute ;
    dct:title "TransactionStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> a ns1:ObjectType ;
    dct:title "Transactions"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> a ns1:Attribute ;
    dct:title "TrueFalseIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#boolean> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalInfo> a ns1:Attribute ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#boolean> a ns1:SimpleType ;
    dct:title "boolean"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber> a ns1:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cardIssuerName> a ns1:Attribute ;
    dct:title "cardIssuerName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#freeText> a ns1:Attribute ;
    dct:title "freeText"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#holderName> a ns1:Attribute ;
    dct:title "holderName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#href> a ns1:Attribute ;
    dct:title "href"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#merchant> a ns1:Attribute ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> a ns1:SimpleType ;
    dct:title "number"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode> a ns1:Attribute ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rel> a ns1:Attribute ;
    dct:title "rel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName> a ns1:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName> a ns1:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#transactionIdentifier> a ns1:Attribute ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0",
        "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
