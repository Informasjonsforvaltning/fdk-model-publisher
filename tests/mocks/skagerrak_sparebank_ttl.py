"""Example TTL output."""
skagerrak_sparebank_ttl_mock = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://fdk-model-publisher.fellesdatakatalog.no> a dcat:Catalog ;
    dct:title "FDK informasjonsmodellkatalog"@nb ;
    ns1:model <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc> .

<https://fdk-model-publisher.fellesdatakatalog.no#937891245> a foaf:Agent ;
    dct:identifier "937891245" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType ;
    dct:title "Accounts API Skagerrak Sparebank" .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc> a ns1:InformationModel ;
    dct:conformsTo <https://data.norge.no/specification/kontoopplysninger> ;
    dct:description "Open API specification of the Account APIs. (Work in progress.)"@en ;
    dct:hasFormat <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> ;
    dct:publisher <https://fdk-model-publisher.fellesdatakatalog.no#937891245> ;
    dct:title "Information Model - Accounts API Skagerrak Sparebank"@en ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountDetails>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Accounts>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Cards>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Roles>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Transactions> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Account> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#accountReference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#primaryOwner>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#servicer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountDetail> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "AccountDetail"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#accountReference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#balances>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#primaryOwner>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#servicer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#startDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountDetails> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "AccountDetails"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetails#account>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetails#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountPermissionType> a ns1:CodeList ;
    dct:title "AccountPermissionType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Accounts> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Accounts"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#accounts>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AddressType> a ns1:CodeList ;
    dct:description "Categorization of ways to use an address according to the type of address the address, as described, is and what you want to do when using the address"@en ;
    dct:title "AddressType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Balance> a ns1:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditDebitIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineAmount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineIncluded>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#registered>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#BalanceType> a ns1:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#BankTransactionCode> a ns1:ObjectType ;
    dct:description "Transaction code"@en ;
    dct:title "BankTransactionCode"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#domain>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#family>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#freeText>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#subFamily> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CardType> a ns1:CodeList ;
    dct:description "Card type"@en ;
    dct:title "CardType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Cards> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Cards"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Cards#paymentCards>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Cards#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CounterParty> a ns1:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#postalAddress>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CounterPartyType> a ns1:CodeList ;
    dct:title "CounterPartyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyExchange> a ns1:ObjectType ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "CurrencyExchange"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#exchangeRate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#originalAmount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#sourceCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#targetCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#unitCurrency> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#DomainType> a ns1:CodeList ;
    dct:title "DomainType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ElectronicAddress> a ns1:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ElectronicAddressType> a ns1:CodeList ;
    dct:title "ElectronicAddressType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#FamilyType> a ns1:CodeList ;
    dct:title "FamilyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#IdentifierType> a ns1:CodeList ;
    dct:title "IdentifierType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Roles> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Roles"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Roles#responseStatus>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Roles#roles> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#SubFamilyType> a ns1:CodeList ;
    dct:title "SubFamilyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Transaction> a ns1:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#additionalInfo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#bookingDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#counterParties>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#creditDebitIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#currencyExchange>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#merchant>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#paymentCard>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#references>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#registered>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#reversalIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#transactionCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#transactionIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#valueDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionReference> a ns1:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/TransactionReference#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/TransactionReference#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionReferenceType> a ns1:CodeList ;
    dct:title "TransactionReferenceType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionStatus> a ns1:CodeList ;
    dct:title "TransactionStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Transactions> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Transactions"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#responseStatus>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#transactions> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#FinancialInstitution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Account/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#balances> a ns1:Role ;
    dct:title "balances"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Balance> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#FinancialInstitution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetail/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetails#account> a ns1:Composition ;
    dct:title "account"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountDetail> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountDetails#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#electronicAddresses> a ns1:Role ;
    dct:title "electronicAddresses"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ElectronicAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#permission> a ns1:Attribute ;
    dct:title "permission"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountPermissionType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PostalAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#accounts> a ns1:Role ;
    dct:title "accounts"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Account> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Accounts#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CreditOrDebit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineAmount> a ns1:Attribute ;
    dct:title "creditLineAmount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineCurrency> a ns1:Attribute ;
    dct:title "creditLineCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#creditLineIncluded> a ns1:Attribute ;
    dct:title "creditLineIncluded"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Balance#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#BalanceType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#domain> a ns1:Attribute ;
    dct:title "domain"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#DomainType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#family> a ns1:Attribute ;
    dct:title "family"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#FamilyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#freeText> a ns1:Attribute ;
    dct:title "freeText"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode/freeText#freeText> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode#subFamily> a ns1:Attribute ;
    dct:title "subFamily"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#SubFamilyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/BankTransactionCode/freeText#freeText> a ns1:SimpleType ;
    dct:title "freeText"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Cards#paymentCards> a ns1:Role ;
    dct:description "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales"@en ;
    dct:title "paymentCards"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PaymentCard> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Cards#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PostalAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CounterPartyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CounterParty/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#exchangeRate> a ns1:Attribute ;
    dct:title "exchangeRate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#originalAmount> a ns1:Attribute ;
    dct:title "originalAmount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#sourceCurrency> a ns1:Attribute ;
    dct:title "sourceCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#targetCurrency> a ns1:Attribute ;
    dct:title "targetCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/CurrencyExchange#unitCurrency> a ns1:Attribute ;
    dct:title "unitCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ElectronicAddressType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress/value#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/ElectronicAddress/value#value> a ns1:SimpleType ;
    dct:title "value"@en ;
    xsd:maxLength 2048 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#countryOfResidence> a ns1:Attribute ;
    dct:title "countryOfResidence"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CountryCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#IdentifierType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link#href> a ns1:Attribute ;
    dct:title "href"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link/href#href> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link#rel> a ns1:Attribute ;
    dct:title "rel"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link/rel#rel> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link/href#href> a ns1:SimpleType ;
    dct:title "href"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link/rel#rel> a ns1:SimpleType ;
    dct:title "rel"@en ;
    xsd:maxLength 50 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIdentifier> a ns1:Attribute ;
    dct:title "cardIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIssuerIdentifier> a ns1:Role ;
    dct:title "cardIssuerIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIssuerName> a ns1:Attribute ;
    dct:description "Card issuers name: The financial institution that has issued a payment card"@en ;
    dct:title "cardIssuerName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard/cardIssuerName#cardIssuerName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#expiryDate> a ns1:Attribute ;
    dct:title "expiryDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ISOYearMonth> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#holderName> a ns1:Attribute ;
    dct:description "Cardholders name: party to whom the payment card is issued"@en ;
    dct:title "holderName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard/holderName#holderName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ISOYearMonth> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CardType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard/cardIssuerName#cardIssuerName> a ns1:SimpleType ;
    dct:title "cardIssuerName"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard/holderName#holderName> a ns1:SimpleType ;
    dct:title "holderName"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#addressLines> a ns1:Attribute ;
    dct:title "addressLines"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/addressLines#addressLines> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#buildingNumber> a ns1:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/buildingNumber#buildingNumber> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#country> a ns1:Attribute ;
    dct:title "country"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CountryCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#postCode> a ns1:Attribute ;
    dct:description "Post code"@en ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/postCode#postCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#streetName> a ns1:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/streetName#streetName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#townName> a ns1:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/townName#townName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AddressType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/addressLines#addressLines> a ns1:SimpleType ;
    dct:title "addressLines"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/buildingNumber#buildingNumber> a ns1:SimpleType ;
    dct:title "buildingNumber"@en ;
    xsd:maxLength 16 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/postCode#postCode> a ns1:SimpleType ;
    dct:title "postCode"@en ;
    xsd:maxLength 16 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/streetName#streetName> a ns1:SimpleType ;
    dct:title "streetName"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress/townName#townName> a ns1:SimpleType ;
    dct:title "townName"@en ;
    xsd:maxLength 35 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Roles#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Roles#roles> a ns1:Role ;
    dct:title "roles"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#additionalInfo> a ns1:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/additionalInfo#additionalInfo> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#bookingDate> a ns1:Attribute ;
    dct:title "bookingDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#counterParties> a ns1:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CounterParty> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CreditOrDebit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#currencyExchange> a ns1:Composition ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "currencyExchange"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyExchange> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#merchant> a ns1:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/merchant#merchant> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#paymentCard> a ns1:Composition ;
    dct:description "Payment Cards: The common term for various types of cards used for cash withdrawals and for the payment of goods and services at different point of sales"@en ;
    dct:title "paymentCard"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PaymentCard> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#references> a ns1:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionReference> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#reversalIndicator> a ns1:Attribute ;
    dct:title "reversalIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#transactionCode> a ns1:Composition ;
    dct:description "Transaction code: contains a set of indicators to identify the type of transaction"@en ;
    dct:title "transactionCode"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#BankTransactionCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#transactionIdentifier> a ns1:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/transactionIdentifier#transactionIdentifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction#valueDate> a ns1:Attribute ;
    dct:title "valueDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/additionalInfo#additionalInfo> a ns1:SimpleType ;
    dct:title "additionalInfo"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/merchant#merchant> a ns1:SimpleType ;
    dct:title "merchant"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transaction/transactionIdentifier#transactionIdentifier> a ns1:SimpleType ;
    dct:title "transactionIdentifier"@en ;
    xsd:minLength 0 ;
    xsd:maxLength 35 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/TransactionReference#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#TransactionReferenceType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/TransactionReference#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#links> a ns1:Role ;
    dct:description "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. "@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Transactions#transactions> a ns1:Role ;
    dct:description "transaction: any posting on account"@en ;
    dct:title "transactions"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Transaction> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountStatus> a ns1:CodeList ;
    dct:title "AccountStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountType> a ns1:CodeList ;
    dct:description "Account type"@en ;
    dct:title "AccountType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CountryCode> a ns1:SimpleType ;
    dct:title "CountryCode"@en ;
    xsd:pattern "[A-Z]{2,2}" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CreditOrDebit> a ns1:CodeList ;
    dct:title "CreditOrDebit"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#FinancialInstitution> a ns1:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/FinancialInstitution#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ISOYearMonth> a ns1:SimpleType ;
    dct:title "ISOYearMonth"@en ;
    xsd:pattern "^[0-9]+-([0][1-9]|1[0-2])$" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PaymentCard> a ns1:ObjectType ;
    dct:description "debit card: Common term for various types of cards used for cash withdrawals and for payment of goods and services on various point of sales"@en ;
    dct:title "PaymentCard"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIssuerIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#cardIssuerName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#expiryDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#holderName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#startDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PaymentCard#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#PostalAddress> a ns1:ObjectType ;
    dct:description "Physical address and location"@en ;
    dct:title "PostalAddress"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#addressLines>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#buildingNumber>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#country>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#postCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#streetName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#townName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/PostalAddress#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#boolean> a ns1:SimpleType ;
    dct:title "boolean"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#AccountRole> a ns1:ObjectType ;
    dct:description "Account role: indicates owner or manager of account"@en ;
    dct:title "AccountRole"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#electronicAddresses>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#permission>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#postalAddress>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/AccountRole#startDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Link> a ns1:ObjectType ;
    dct:title "Link"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link#href>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Link#rel> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Identifier> a ns1:ObjectType ;
    dct:description "Specific data that assist in identifying the object"@en ;
    dct:title "Identifier"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#countryOfResidence>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc/Identifier#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date> a ns1:SimpleType ;
    dct:title "date"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#date-time> a ns1:SimpleType ;
    dct:title "date-time"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#Amount> a ns1:SimpleType ;
    dct:title "Amount"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#ResponseStatus> a ns1:CodeList ;
    dct:title "ResponseStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#CurrencyCode> a ns1:SimpleType ;
    dct:title "CurrencyCode"@en ;
    xsd:pattern "[A-Z]{3,3}" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/3f04e254cc0058a6826ada4a238d90104a80f4dc#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
