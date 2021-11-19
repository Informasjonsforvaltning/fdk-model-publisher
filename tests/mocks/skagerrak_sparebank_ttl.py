"""Example TTL output."""
skagerrak_sparebank_ttl_mock = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://fdk-model-publisher.fellesdatakatalog.no> a dcat:Catalog ;
    dct:title "FDK informasjonsmodellkatalog"@nb ;
    ns1:model <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8> .

<https://fdk-model-publisher.fellesdatakatalog.no#937891245> a foaf:Agent ;
    dct:identifier "937891245" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType ;
    dct:title "Accounts API Skagerrak Sparebank" .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8> a ns1:InformationModel ;
    dct:conformsTo <https://data.norge.no/specification/kontoopplysninger> ;
    dct:description "Open API specification of the Account APIs. (Work in progress.)"@en ;
    dct:hasFormat <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> ;
    dct:publisher <https://fdk-model-publisher.fellesdatakatalog.no#937891245> ;
    dct:title "Information Model - Accounts API Skagerrak Sparebank"@en ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountDetails>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Accounts>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Cards>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Roles>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Transactions> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Account> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#accountReference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#primaryOwner>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#servicer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountDetail> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "AccountDetail"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#accountReference>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#balances>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#primaryOwner>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#servicer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#startDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountDetails> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "AccountDetails"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetails#account>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetails#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountPermissionType> a ns1:CodeList ;
    dct:title "AccountPermissionType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Accounts> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Accounts"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#accounts>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AddressType> a ns1:CodeList ;
    dct:description "Categorization of ways to use an address according to the type of address the address, as described, is and what you want to do when using the address"@en ;
    dct:title "AddressType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Balance> a ns1:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditDebitIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineAmount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineIncluded>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#registered>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#BalanceType> a ns1:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#BankTransactionCode> a ns1:ObjectType ;
    dct:description "Transaction code"@en ;
    dct:title "BankTransactionCode"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#domain>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#family>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#freeText>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#subFamily> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CardType> a ns1:CodeList ;
    dct:description "Card type"@en ;
    dct:title "CardType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Cards> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Cards"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Cards#paymentCards>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Cards#responseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CounterParty> a ns1:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#accountIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#postalAddress>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CounterPartyType> a ns1:CodeList ;
    dct:title "CounterPartyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyExchange> a ns1:ObjectType ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "CurrencyExchange"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#exchangeRate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#originalAmount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#sourceCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#targetCurrency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#unitCurrency> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#DomainType> a ns1:CodeList ;
    dct:title "DomainType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ElectronicAddress> a ns1:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ElectronicAddressType> a ns1:CodeList ;
    dct:title "ElectronicAddressType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#FamilyType> a ns1:CodeList ;
    dct:title "FamilyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#IdentifierType> a ns1:CodeList ;
    dct:title "IdentifierType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Roles> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Roles"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Roles#responseStatus>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Roles#roles> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#SubFamilyType> a ns1:CodeList ;
    dct:title "SubFamilyType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Transaction> a ns1:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#additionalInfo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#bookingDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#counterParties>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#creditDebitIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#currency>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#currencyExchange>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#merchant>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#paymentCard>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#references>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#registered>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#reversalIndicator>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#status>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#transactionCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#transactionIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#valueDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionReference> a ns1:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/TransactionReference#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/TransactionReference#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionReferenceType> a ns1:CodeList ;
    dct:title "TransactionReferenceType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionStatus> a ns1:CodeList ;
    dct:title "TransactionStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Transactions> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Transactions"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#links>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#responseStatus>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#transactions> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#FinancialInstitution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Account/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#balances> a ns1:Role ;
    dct:title "balances"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Balance> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#FinancialInstitution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetail/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetails#account> a ns1:Composition ;
    dct:title "account"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountDetail> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountDetails#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#electronicAddresses> a ns1:Role ;
    dct:title "electronicAddresses"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ElectronicAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#permission> a ns1:Attribute ;
    dct:title "permission"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountPermissionType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PostalAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#accounts> a ns1:Role ;
    dct:title "accounts"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Account> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Accounts#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CreditOrDebit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineAmount> a ns1:Attribute ;
    dct:title "creditLineAmount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineCurrency> a ns1:Attribute ;
    dct:title "creditLineCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#creditLineIncluded> a ns1:Attribute ;
    dct:title "creditLineIncluded"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Balance#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#BalanceType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#domain> a ns1:Attribute ;
    dct:title "domain"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#DomainType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#family> a ns1:Attribute ;
    dct:title "family"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#FamilyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#freeText> a ns1:Attribute ;
    dct:title "freeText"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode/freeText#freeText> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode#subFamily> a ns1:Attribute ;
    dct:title "subFamily"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#SubFamilyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/BankTransactionCode/freeText#freeText> a ns1:SimpleType ;
    dct:title "freeText"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Cards#paymentCards> a ns1:Role ;
    dct:description "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales"@en ;
    dct:title "paymentCards"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PaymentCard> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Cards#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PostalAddress> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CounterPartyType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CounterParty/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#exchangeRate> a ns1:Attribute ;
    dct:title "exchangeRate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#originalAmount> a ns1:Attribute ;
    dct:title "originalAmount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#sourceCurrency> a ns1:Attribute ;
    dct:title "sourceCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#targetCurrency> a ns1:Attribute ;
    dct:title "targetCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/CurrencyExchange#unitCurrency> a ns1:Attribute ;
    dct:title "unitCurrency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ElectronicAddressType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress/value#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/ElectronicAddress/value#value> a ns1:SimpleType ;
    dct:title "value"@en ;
    xsd:maxLength 2048 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution/name#name> a ns1:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#countryOfResidence> a ns1:Attribute ;
    dct:title "countryOfResidence"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CountryCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#IdentifierType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link#href> a ns1:Attribute ;
    dct:title "href"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link/href#href> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link#rel> a ns1:Attribute ;
    dct:title "rel"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link/rel#rel> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link/href#href> a ns1:SimpleType ;
    dct:title "href"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link/rel#rel> a ns1:SimpleType ;
    dct:title "rel"@en ;
    xsd:maxLength 50 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIdentifier> a ns1:Attribute ;
    dct:title "cardIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIssuerIdentifier> a ns1:Role ;
    dct:title "cardIssuerIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Identifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIssuerName> a ns1:Attribute ;
    dct:description "Card issuers name: The financial institution that has issued a payment card"@en ;
    dct:title "cardIssuerName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard/cardIssuerName#cardIssuerName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#expiryDate> a ns1:Attribute ;
    dct:title "expiryDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ISOYearMonth> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#holderName> a ns1:Attribute ;
    dct:description "Cardholders name: party to whom the payment card is issued"@en ;
    dct:title "holderName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard/holderName#holderName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ISOYearMonth> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CardType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard/cardIssuerName#cardIssuerName> a ns1:SimpleType ;
    dct:title "cardIssuerName"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard/holderName#holderName> a ns1:SimpleType ;
    dct:title "holderName"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#addressLines> a ns1:Attribute ;
    dct:title "addressLines"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/addressLines#addressLines> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#buildingNumber> a ns1:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/buildingNumber#buildingNumber> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#country> a ns1:Attribute ;
    dct:title "country"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CountryCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#postCode> a ns1:Attribute ;
    dct:description "Post code"@en ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/postCode#postCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#streetName> a ns1:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/streetName#streetName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#townName> a ns1:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/townName#townName> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AddressType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/addressLines#addressLines> a ns1:SimpleType ;
    dct:title "addressLines"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/buildingNumber#buildingNumber> a ns1:SimpleType ;
    dct:title "buildingNumber"@en ;
    xsd:maxLength 16 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/postCode#postCode> a ns1:SimpleType ;
    dct:title "postCode"@en ;
    xsd:maxLength 16 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/streetName#streetName> a ns1:SimpleType ;
    dct:title "streetName"@en ;
    xsd:maxLength 70 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress/townName#townName> a ns1:SimpleType ;
    dct:title "townName"@en ;
    xsd:maxLength 35 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Roles#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Roles#roles> a ns1:Role ;
    dct:title "roles"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountRole> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#additionalInfo> a ns1:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/additionalInfo#additionalInfo> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#bookingDate> a ns1:Attribute ;
    dct:title "bookingDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#counterParties> a ns1:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CounterParty> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CreditOrDebit> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#currencyExchange> a ns1:Composition ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "currencyExchange"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyExchange> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#merchant> a ns1:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/merchant#merchant> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#paymentCard> a ns1:Composition ;
    dct:description "Payment Cards: The common term for various types of cards used for cash withdrawals and for the payment of goods and services at different point of sales"@en ;
    dct:title "paymentCard"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PaymentCard> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#references> a ns1:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionReference> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#reversalIndicator> a ns1:Attribute ;
    dct:title "reversalIndicator"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#boolean> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#transactionCode> a ns1:Composition ;
    dct:description "Transaction code: contains a set of indicators to identify the type of transaction"@en ;
    dct:title "transactionCode"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#BankTransactionCode> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#transactionIdentifier> a ns1:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/transactionIdentifier#transactionIdentifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction#valueDate> a ns1:Attribute ;
    dct:title "valueDate"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date-time> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/additionalInfo#additionalInfo> a ns1:SimpleType ;
    dct:title "additionalInfo"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/merchant#merchant> a ns1:SimpleType ;
    dct:title "merchant"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transaction/transactionIdentifier#transactionIdentifier> a ns1:SimpleType ;
    dct:title "transactionIdentifier"@en ;
    xsd:minLength 0 ;
    xsd:maxLength 35 ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/TransactionReference#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#TransactionReferenceType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/TransactionReference#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#links> a ns1:Role ;
    dct:description "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. "@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Link> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> ;
    ns1:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Transactions#transactions> a ns1:Role ;
    dct:description "transaction: any posting on account"@en ;
    dct:title "transactions"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Transaction> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountStatus> a ns1:CodeList ;
    dct:title "AccountStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountType> a ns1:CodeList ;
    dct:description "Account type"@en ;
    dct:title "AccountType"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CountryCode> a ns1:SimpleType ;
    dct:title "CountryCode"@en ;
    xsd:pattern "[A-Z]{2,2}" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CreditOrDebit> a ns1:CodeList ;
    dct:title "CreditOrDebit"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#FinancialInstitution> a ns1:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/FinancialInstitution#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ISOYearMonth> a ns1:SimpleType ;
    dct:title "ISOYearMonth"@en ;
    xsd:pattern "^[0-9]+-([0][1-9]|1[0-2])$" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PaymentCard> a ns1:ObjectType ;
    dct:description "debit card: Common term for various types of cards used for cash withdrawals and for payment of goods and services on various point of sales"@en ;
    dct:title "PaymentCard"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIssuerIdentifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#cardIssuerName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#expiryDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#holderName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#startDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PaymentCard#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#PostalAddress> a ns1:ObjectType ;
    dct:description "Physical address and location"@en ;
    dct:title "PostalAddress"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#addressLines>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#buildingNumber>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#country>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#postCode>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#streetName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#townName>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/PostalAddress#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#boolean> a ns1:SimpleType ;
    dct:title "boolean"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#AccountRole> a ns1:ObjectType ;
    dct:description "Account role: indicates owner or manager of account"@en ;
    dct:title "AccountRole"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#electronicAddresses>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#endDate>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#identifier>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#name>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#permission>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#postalAddress>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/AccountRole#startDate> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Link> a ns1:ObjectType ;
    dct:title "Link"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link#href>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Link#rel> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Identifier> a ns1:ObjectType ;
    dct:description "Specific data that assist in identifying the object"@en ;
    dct:title "Identifier"@en ;
    ns1:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#countryOfResidence>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#type>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8/Identifier#value> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date> a ns1:SimpleType ;
    dct:title "date"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#date-time> a ns1:SimpleType ;
    dct:title "date-time"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#Amount> a ns1:SimpleType ;
    dct:title "Amount"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#ResponseStatus> a ns1:CodeList ;
    dct:title "ResponseStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#CurrencyCode> a ns1:SimpleType ;
    dct:title "CurrencyCode"@en ;
    xsd:pattern "[A-Z]{3,3}" ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/fc1326201eb8f4e7ea074270e62119d938e1fee8#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    ns1:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
