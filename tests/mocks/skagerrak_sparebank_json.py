skagerrak_sparebank_json_mock = """
{
  "openapi": "3.0.0",
  "info": {
    "description": "Open API specification of the Account APIs. (Work in progress.)",
    "version": "1.0.0",
    "title": "Accounts API Skagerrak Sparebank"
  },
  "servers": [
    {
      "url": "https://api-proxy.sdc.dk/api/dsop-accounts-api/v1/banks/937891245",
      "description": "production"
    }
  ],
  "paths": {
    "/accounts": {
      "get": {
        "summary": "List of accounts for a specified party and period. Account number can be provided in place of the party identifier for lookup requests directly on the account. Must provide a blank list if no hits.",
        "operationId": "listAccounts",
        "tags": [
          "accounts"
        ],
        "parameters": [
          {
            "name": "fromDate",
            "in": "query",
            "description": "From date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "To date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "header",
            "name": "CorrelationID",
            "description": "Correlation ID, unique identifier for the technical request",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "Legal-Mandate",
            "in": "header",
            "description": "Legal basis that banks should validate",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "PartyID",
            "in": "header",
            "description": "Parts identifier, personal identification number, d number or organization number.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "AccountID",
            "in": "header",
            "description": "The account number",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Valid response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Accounts"
                }
              },
              "application/jose": {
                "schema": {
                  "type": "string",
                  "format": "byte",
                  "description": "Encrypted response according to JWE compact serialization",
                  "example": "(JWE response with content as defined above)"
                }
              }
            }
          },
          "400": {
            "description": "ACC-001 Bad request. The request contains invalid parameters",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error400"
                }
              }
            }
          },
          "401": {
            "description": "ACC-010 Unauthorized. The request is missing authentication information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error401"
                }
              }
            }
          },
          "403": {
            "description": "ACC-011 Forbidden. The user is not authorized for the requested service",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error403"
                }
              }
            }
          },
          "405": {
            "description": "ACC-012 Method Not Allowed. Invalid HTTP method, only GET is supported",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error405"
                }
              }
            }
          },
          "429": {
            "description": "ACC-022 Too many requests. Too many requests, can be given if one chooses to impose rate-limiting on the services to limit the number of requests from a client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error429"
                }
              }
            }
          },
          "500": {
            "description": "ACC-100 Internal server error. Various technical errors on service provider side.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error500"
                }
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    },
    "/accounts/{accountReference}": {
      "get": {
        "summary": "Account details, including balances, for an account",
        "operationId": "showAccountById",
        "tags": [
          "accounts"
        ],
        "parameters": [
          {
            "name": "fromDate",
            "in": "query",
            "description": "From date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "To date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "header",
            "name": "CorrelationID",
            "description": "Correlation ID, unique identifier for the technical request",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "Legal-Mandate",
            "in": "header",
            "description": "Legal basis that banks should validate",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "accountReference",
            "in": "path",
            "description": "Unique reference to the account.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Valid response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AccountDetails"
                }
              },
              "application/jose": {
                "schema": {
                  "type": "string",
                  "format": "byte",
                  "description": "Encrypted response according to JWE compact serialization",
                  "example": "(JWE response with content as defined for AccountDetails)"
                }
              }
            }
          },
          "400": {
            "description": "ACC-001 Bad request. The request contains invalid parameters",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error400"
                }
              }
            }
          },
          "401": {
            "description": "ACC-010 Unauthorized. The request is missing authentication information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error401"
                }
              }
            }
          },
          "403": {
            "description": "ACC-011 Forbidden. The user is not authorized for the requested service",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error403"
                }
              }
            }
          },
          "404": {
            "description": "ACC-002 Resource not found. No information is available for the requested account id",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error404"
                }
              }
            }
          },
          "405": {
            "description": "ACC-012 Method Not Allowed. Invalid HTTP method, only GET is supported",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error405"
                }
              }
            }
          },
          "429": {
            "description": "ACC-022 Too many requests. Too many requests, can be given if one chooses to impose rate-limiting on the services to limit the number of requests from a client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error429"
                }
              }
            }
          },
          "500": {
            "description": "ACC-100 Internal server error. Various technical errors on service provider side.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error500"
                }
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    },
    "/accounts/{accountReference}/transactions": {
      "get": {
        "summary": "Transactions for specified account and period. Empty list if no hits. Must support pagination on large result sets (min 1000) - see separate description in the link element.",
        "operationId": "listTransactions",
        "tags": [
          "transactions"
        ],
        "parameters": [
          {
            "name": "accountReference",
            "in": "path",
            "description": "Unique reference to the account. Cannot match the account number.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "fromDate",
            "in": "query",
            "description": "From date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "To date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "header",
            "name": "CorrelationID",
            "description": "Correlation ID, unique identifier for the technical request",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "Legal-Mandate",
            "in": "header",
            "description": "Legal basis",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A list of transactions",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Transactions"
                }
              },
              "application/jose": {
                "schema": {
                  "type": "string",
                  "format": "byte",
                  "description": "Encrypted response according to JWE compact serialization",
                  "example": "(JWE response with content as defined above)"
                }
              }
            }
          },
          "400": {
            "description": "ACC-001 Bad request. The request contains invalid parameters",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error400"
                }
              }
            }
          },
          "401": {
            "description": "ACC-010 Unauthorized. The request is missing authentication information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error401"
                }
              }
            }
          },
          "403": {
            "description": "ACC-011 Forbidden. The user is not authorized for the requested service",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error403"
                }
              }
            }
          },
          "405": {
            "description": "ACC-012 Method Not Allowed. Invalid HTTP method, only GET is supported",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error405"
                }
              }
            }
          },
          "429": {
            "description": "ACC-022 Too many requests. Too many requests, can be given if one chooses to impose rate-limiting on the services to limit the number of requests from a client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error429"
                }
              }
            }
          },
          "500": {
            "description": "ACC-100 Internal server error. Various technical errors on service provider side.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error500"
                }
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    },
    "/accounts/{accountReference}/cards": {
      "get": {
        "summary": "List of cards associated with the specified account. Empty list if no hits.",
        "operationId": "listCards",
        "tags": [
          "cards"
        ],
        "parameters": [
          {
            "name": "accountReference",
            "in": "path",
            "description": "Unique reference to the account. Cannot match the account number.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "fromDate",
            "in": "query",
            "description": "From date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "To date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "header",
            "name": "CorrelationID",
            "description": "Correlation ID, unique identifier for the technical request",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "Legal-Mandate",
            "in": "header",
            "description": "Legal basis",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Valid response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Cards"
                }
              },
              "application/jose": {
                "schema": {
                  "type": "string",
                  "format": "byte",
                  "description": "Encrypted response according to JWE compact serialization",
                  "example": "(JWE response with as content defined above)"
                }
              }
            }
          },
          "400": {
            "description": "ACC-001 Bad request. The request contains invalid parameters",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error400"
                }
              }
            }
          },
          "401": {
            "description": "ACC-010 Unauthorized. The request is missing authentication information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error401"
                }
              }
            }
          },
          "403": {
            "description": "ACC-011 Forbidden. The user is not authorized for the requested service",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error403"
                }
              }
            }
          },
          "405": {
            "description": "ACC-012 Method Not Allowed. Invalid HTTP method, only GET is supported",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error405"
                }
              }
            }
          },
          "429": {
            "description": "ACC-022 Too many requests. Too many requests, can be given if one chooses to impose rate-limiting on the services to limit the number of requests from a client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error429"
                }
              }
            }
          },
          "500": {
            "description": "ACC-100 Internal server error. Various technical errors on service provider side.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error500"
                }
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    },
    "/accounts/{accountReference}/roles": {
      "get": {
        "summary": "Role holders for the specified account. Empty list if no hits.",
        "operationId": "listRoles",
        "tags": [
          "roles"
        ],
        "parameters": [
          {
            "name": "accountReference",
            "in": "path",
            "description": "Unique reference to the account. Cannot match the account number.",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "fromDate",
            "in": "query",
            "description": "From date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "toDate",
            "in": "query",
            "description": "To date, current date if not stated",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "header",
            "name": "CorrelationID",
            "description": "Correlation ID, unique identifier for the technical request",
            "required": true,
            "schema": {
              "type": "string",
              "format": "uuid"
            }
          },
          {
            "name": "Legal-Mandate",
            "in": "header",
            "description": "Legal basis",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Valid response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Roles"
                }
              },
              "application/jose": {
                "schema": {
                  "type": "string",
                  "format": "byte",
                  "description": "Encrypted response according to JWE compact serialization",
                  "example": "(JWE response with content as defined above)"
                }
              }
            }
          },
          "400": {
            "description": "ACC-001 Bad request. The request contains invalid parameters",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error400"
                }
              }
            }
          },
          "401": {
            "description": "ACC-010 Unauthorized. The request is missing authentication information",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error401"
                }
              }
            }
          },
          "403": {
            "description": "ACC-011 Forbidden. The user is not authorized for the requested service",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error403"
                }
              }
            }
          },
          "405": {
            "description": "ACC-012 Method Not Allowed. Invalid HTTP method, only GET is supported ",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error405"
                }
              }
            }
          },
          "429": {
            "description": "ACC-022 Too many requests. Too many requests, can be given if one chooses to impose rate-limiting on the services to limit the number of requests from a client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error429"
                }
              }
            }
          },
          "500": {
            "description": "ACC-100 Internal server error. Various technical errors on service provider side.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error500"
                }
              }
            }
          },
          "default": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "accountsAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "Access token (JWT)"
      }
    },
    "schemas": {
      "Account": {
        "description": "Account: a specification of a clearly defined type of financial events",
        "required": [
          "accountIdentifier",
          "accountReference",
          "type",
          "status",
          "currency",
          "servicer",
          "primaryOwner"
        ],
        "type": "object",
        "properties": {
          "status": {
            "description": "Status: indicates current account status",
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountStatus"
              }
            ]
          },
          "servicer": {
            "description": "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account",
            "allOf": [
              {
                "$ref": "#/components/schemas/FinancialInstitution"
              }
            ]
          },
          "links": {
            "type": "array",
            "items": {
              "description": "Pagination: dividing the result into pages for large resultsets",
              "allOf": [
                {
                  "$ref": "#/components/schemas/Link"
                }
              ]
            },
            "minItems": 0
          },
          "accountIdentifier": {
            "$ref": "#/components/schemas/AccountNumber"
          },
          "accountReference": {
            "$ref": "#/components/schemas/AccountReference"
          },
          "type": {
            "$ref": "#/components/schemas/AccountType"
          },
          "currency": {
            "$ref": "#/components/schemas/CurrencyCode"
          },
          "primaryOwner": {
            "$ref": "#/components/schemas/AccountRole"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 70
          }
        }
      },
      "AccountDetail": {
        "description": "Account: a specification of a clearly defined type of financial events",
        "required": [
          "accountIdentifier",
          "accountReference",
          "type",
          "status",
          "currency",
          "servicer",
          "primaryOwner"
        ],
        "type": "object",
        "properties": {
          "status": {
            "description": "Status: indicates current account status",
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountStatus"
              }
            ]
          },
          "servicer": {
            "description": "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account",
            "allOf": [
              {
                "$ref": "#/components/schemas/FinancialInstitution"
              }
            ]
          },
          "accountIdentifier": {
            "$ref": "#/components/schemas/AccountNumber"
          },
          "accountReference": {
            "$ref": "#/components/schemas/AccountReference"
          },
          "type": {
            "$ref": "#/components/schemas/AccountType"
          },
          "currency": {
            "$ref": "#/components/schemas/CurrencyCode"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 70
          },
          "balances": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Balance"
            },
            "minItems": 0
          },
          "primaryOwner": {
            "$ref": "#/components/schemas/AccountRole"
          },
          "startDate": {
            "$ref": "#/components/schemas/ISODate"
          },
          "endDate": {
            "$ref": "#/components/schemas/ISODate"
          }
        }
      },
      "AccountDetails": {
        "description": "Root element for response",
        "type": "object",
        "properties": {
          "responseStatus": {
            "description": "Indicates whether this is a complete response or whether there is also offline data that cannot be retrieved through the api.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ResponseStatus"
              }
            ]
          },
          "account": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountDetail"
              }
            ]
          }
        },
        "xml": {
          "name": "accounts"
        }
      },
      "AccountNumber": {
        "description": "Account number",
        "type": "string"
      },
      "AccountPermissionType": {
        "enum": [
          "noRight",
          "rightToUseAlone",
          "rightToUseWithOther"
        ],
        "type": "string"
      },
      "AccountRole": {
        "description": "Account role: indicates owner or manager of account",
        "type": "object",
        "properties": {
          "permission": {
            "description": "Account permissions: specifies the rights to an account",
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountPermissionType"
              }
            ]
          },
          "identifier": {
            "$ref": "#/components/schemas/Identifier"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          },
          "startDate": {
            "$ref": "#/components/schemas/ISODate"
          },
          "endDate": {
            "$ref": "#/components/schemas/ISODate"
          },
          "postalAddress": {
            "$ref": "#/components/schemas/PostalAddress"
          },
          "electronicAddresses": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ElectronicAddress"
            },
            "minItems": 0
          }
        },
        "required": [
          "name"
        ]
      },
      "AccountReference": {
        "description": "accountReference - Unique reference to the account. Should not contain sensitive information such as account number",
        "type": "string"
      },
      "Accounts": {
        "description": "Root element for response",
        "type": "object",
        "properties": {
          "responseStatus": {
            "description": "Indicates whether this is a complete response or whether there are also offline data that cannot be retrieved through the api.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ResponseStatus"
              }
            ]
          },
          "accounts": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Account"
            },
            "minItems": 0
          },
          "links": {
            "type": "array",
            "items": {
              "description": "Pagination: dividing the result into pages for large resultsets",
              "allOf": [
                {
                  "$ref": "#/components/schemas/Link"
                }
              ]
            },
            "minItems": 0
          }
        },
        "xml": {
          "name": "accounts"
        }
      },
      "AccountStatus": {
        "enum": [
          "enabled",
          "disabled",
          "deleted"
        ],
        "type": "string"
      },
      "AccountType": {
        "description": "Account type",
        "enum": [
          "loanAccount",
          "salaryAccount",
          "currencyAccount",
          "savingsAccount",
          "clientAccount",
          "taxDeductionAccount",
          "businessAccount"
        ],
        "type": "string"
      },
      "AddressType": {
        "description": "Categorization of ways to use an address according to the type of address the address, as described, is and what you want to do when using the address",
        "enum": [
          "residential",
          "business",
          "mailTo",
          "deliveryTo"
        ],
        "type": "string"
      },
      "Amount": {
        "description": "Amount, always as positive value. CreditDebitIndicator should be used to indicate whether the amount is positive or negative.",
        "type": "number",
        "minimum": 0,
        "exclusiveMinimum": false
      },
      "Balance": {
        "description": "Balance: Sum of deposits and loans in the financial account",
        "required": [
          "type",
          "creditLineIncluded",
          "amount",
          "currency",
          "creditDebitIndicator",
          "registered"
        ],
        "type": "object",
        "properties": {
          "creditLineIncluded": {
            "description": "Balance included credit limit: Indicates whether the credit limit is included in the balance or not. Should always be false",
            "allOf": [
              {
                "$ref": "#/components/schemas/TrueFalseIndicator"
              }
            ]
          },
          "amount": {
            "description": "A sum of money spent in a context. This can be a transaction, balance etc.",
            "allOf": [
              {
                "$ref": "#/components/schemas/Amount"
              }
            ]
          },
          "creditDebitIndicator": {
            "description": "Credit is positive balance, debit is negative balance",
            "allOf": [
              {
                "$ref": "#/components/schemas/CreditOrDebit"
              }
            ]
          },
          "registered": {
            "description": "registration date: the current date and time of the reported balance",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISODateTime"
              }
            ]
          },
          "type": {
            "$ref": "#/components/schemas/BalanceType"
          },
          "creditLineAmount": {
            "$ref": "#/components/schemas/Amount"
          },
          "creditLineCurrency": {
            "$ref": "#/components/schemas/CurrencyCode"
          },
          "currency": {
            "$ref": "#/components/schemas/CurrencyCode"
          }
        }
      },
      "BalanceType": {
        "description": "Balance type",
        "enum": [
          "availableBalance",
          "bookedBalance"
        ],
        "type": "string"
      },
      "BankTransactionCode": {
        "description": "Transaction code",
        "type": "object",
        "properties": {
          "domain": {
            "description": "Business area: High level classification of the activity in a business",
            "allOf": [
              {
                "$ref": "#/components/schemas/DomainType"
              }
            ]
          },
          "family": {
            "description": "Product: the specification of a product",
            "allOf": [
              {
                "$ref": "#/components/schemas/FamilyType"
              }
            ]
          },
          "subFamily": {
            "description": "Sub-product: Detailing of a product",
            "allOf": [
              {
                "$ref": "#/components/schemas/SubFamilyType"
              }
            ]
          },
          "freeText": {
            "type": "string",
            "minLength": 1,
            "maxLength": 500
          }
        }
      },
      "CardNumber": {
        "description": "Masked card number",
        "type": "string"
      },
      "Cards": {
        "description": "Root element for response",
        "type": "object",
        "xml": {
          "name": "cards"
        },
        "properties": {
          "responseStatus": {
            "description": "Indicates whether this is a complete response or whether there are also offline data that cannot be retrieved through the api.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ResponseStatus"
              }
            ]
          },
          "paymentCards": {
            "type": "array",
            "items": {
              "description": "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales",
              "allOf": [
                {
                  "$ref": "#/components/schemas/PaymentCard"
                }
              ]
            },
            "minItems": 0
          }
        }
      },
      "CardType": {
        "description": "Card type",
        "enum": [
          "creditCard",
          "debitCard"
        ],
        "type": "string"
      },
      "CounterParty": {
        "description": "Counterparty: the party to which a transaction goes to or comes from",
        "type": "object",
        "properties": {
          "accountIdentifier": {
            "$ref": "#/components/schemas/AccountNumber"
          },
          "identifier": {
            "$ref": "#/components/schemas/Identifier"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          },
          "type": {
            "$ref": "#/components/schemas/CounterPartyType"
          },
          "postalAddress": {
            "$ref": "#/components/schemas/PostalAddress"
          }
        },
        "required": [
          "type"
        ]
      },
      "CounterPartyType": {
        "enum": [
          "debtor",
          "creditor",
          "ultimateDebtor",
          "ultimateCreditor"
        ],
        "type": "string"
      },
      "CountryCode": {
        "description": "Country code, ISO 3166-1 (alfa-2)",
        "type": "string",
        "pattern": "[A-Z]{2,2}"
      },
      "CreditOrDebit": {
        "enum": [
          "credit",
          "debit"
        ],
        "type": "string"
      },
      "CurrencyCode": {
        "type": "string",
        "pattern": "[A-Z]{3,3}"
      },
      "CurrencyExchange": {
        "description": "Currency conversion: conversion of an amount from one currency to another",
        "type": "object",
        "properties": {
          "originalAmount": {
            "description": "Amount in the original currency when converting from / to another currency has taken place",
            "allOf": [
              {
                "$ref": "#/components/schemas/Amount"
              }
            ]
          },
          "sourceCurrency": {
            "description": "Source Currency: The currency an amount is to be converted from during a currency conversion",
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyCode"
              }
            ]
          },
          "targetCurrency": {
            "description": "Target currency: The currency an amount is to be converted into during a currency conversion",
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyCode"
              }
            ]
          },
          "unitCurrency": {
            "description": "unit currency: The resulting currency following a currency conversion",
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyCode"
              }
            ]
          },
          "exchangeRate": {
            "$ref": "#/components/schemas/Amount"
          }
        },
        "required": [
          "sourceCurrency",
          "targetCurrency",
          "exchangeRate"
        ]
      },
      "DomainType": {
        "enum": [
          "accountManagement",
          "cashManagement",
          "foreignExchange",
          "payments",
          "securities",
          "tradeServices",
          "extended"
        ],
        "type": "string"
      },
      "ElectronicAddress": {
        "required": [
          "type",
          "value"
        ],
        "type": "object",
        "properties": {
          "type": {
            "$ref": "#/components/schemas/ElectronicAddressType"
          },
          "value": {
            "type": "string",
            "minLength": 1,
            "maxLength": 2048
          }
        }
      },
      "ElectronicAddressType": {
        "enum": [
          "phoneNumber",
          "emailAddress"
        ],
        "type": "string"
      },
      "FamilyType": {
        "enum": [
          "additionalMiscellaneousCreditOperations",
          "additionalMiscellaneousDebitOperations",
          "miscellaneousCreditOperations",
          "miscellaneousDebitOperations",
          "openingAndClosing",
          "accountBalancing",
          "cashPooling",
          "notAvailable",
          "customerCardTransactions",
          "counterTransactions",
          "drafts",
          "issuedCashConcentrationTransactions",
          "issuedCreditTransfers",
          "issuedCheques",
          "issuedDirectDebits",
          "lockboxTransactions",
          "merchantCardTransactions",
          "other",
          "receivedCashConcentrationTransactions",
          "receivedCreditTransfers",
          "receivedCheques",
          "receivedDirectDebits",
          "corporateAction",
          "documentaryCollection",
          "standByLetterOfCredit"
        ],
        "type": "string"
      },
      "FinancialInstitution": {
        "description": "financial institution: Business or other institution involved in finance and banking",
        "required": [
          "identifier",
          "name"
        ],
        "type": "object",
        "properties": {
          "identifier": {
            "$ref": "#/components/schemas/Identifier"
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          }
        }
      },
      "Identifier": {
        "description": "Specific data that assist in identifying the object",
        "type": "object",
        "properties": {
          "countryOfResidence": {
            "description": "Country of residence: the country of residence of the object",
            "allOf": [
              {
                "$ref": "#/components/schemas/CountryCode"
              }
            ]
          },
          "value": {
            "type": "string"
          },
          "type": {
            "$ref": "#/components/schemas/IdentifierType"
          }
        },
        "required": [
          "value",
          "type"
        ]
      },
      "IdentifierType": {
        "enum": [
          "countryIdentificationCode",
          "nationalIdentityNumber"
        ],
        "type": "string"
      },
      "ISODate": {
        "type": "string",
        "format": "date"
      },
      "ISODateTime": {
        "description": "ISO DateTime: YYYY-MM-DDThh:mm:ssZ for UTC or YYYY-MM-DDThh:mm:ss+hh for other timezones",
        "type": "string",
        "format": "date-time"
      },
      "ISOYearMonth": {
        "type": "string",
        "pattern": "^[0-9]+-([0][1-9]|1[0-2])$"
      },
      "Link": {
        "required": [
          "rel",
          "href"
        ],
        "type": "object",
        "properties": {
          "rel": {
            "type": "string",
            "minLength": 1,
            "maxLength": 50
          },
          "href": {
            "type": "string",
            "minLength": 1,
            "maxLength": 500
          }
        }
      },
      "PaymentCard": {
        "description": "debit card: Common term for various types of cards used for cash withdrawals and for payment of goods and services on various point of sales",
        "required": [
          "cardIdentifier",
          "type",
          "holderName",
          "startDate",
          "expiryDate",
          "cardIssuerName"
        ],
        "type": "object",
        "properties": {
          "cardIdentifier": {
            "description": "Card number: number used to identify debit cards. Must be masked",
            "allOf": [
              {
                "$ref": "#/components/schemas/CardNumber"
              }
            ]
          },
          "holderName": {
            "description": "Cardholders name: party to whom the payment card is issued",
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          },
          "startDate": {
            "description": "start date: Indicates the month and year a payment card is valid from",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISOYearMonth"
              }
            ]
          },
          "expiryDate": {
            "description": "Expiration date: Indicates the month and year a payment card is valid until",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISOYearMonth"
              }
            ]
          },
          "cardIssuerName": {
            "description": "Card issuers name: The financial institution that has issued a payment card",
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          },
          "type": {
            "$ref": "#/components/schemas/CardType"
          },
          "cardIssuerIdentifier": {
            "$ref": "#/components/schemas/Identifier"
          }
        }
      },
      "PostalAddress": {
        "description": "Physical address and location",
        "type": "object",
        "properties": {
          "postCode": {
            "description": "Post code",
            "type": "string",
            "minLength": 1,
            "maxLength": 16
          },
          "type": {
            "$ref": "#/components/schemas/AddressType"
          },
          "streetName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 70
          },
          "buildingNumber": {
            "type": "string",
            "minLength": 1,
            "maxLength": 16
          },
          "townName": {
            "type": "string",
            "minLength": 1,
            "maxLength": 35
          },
          "country": {
            "$ref": "#/components/schemas/CountryCode"
          },
          "addressLines": {
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1,
              "maxLength": 70
            },
            "minItems": 0
          }
        },
        "required": [
          "type"
        ]
      },
      "ResponseStatus": {
        "type": "string",
        "enum": [
          "partial",
          "complete"
        ]
      },
      "Roles": {
        "description": "Root element for response",
        "type": "object",
        "xml": {
          "name": "roles"
        },
        "properties": {
          "responseStatus": {
            "description": "Indicates whether this is a complete response or whether there are also offline data that cannot be retrieved through the api.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ResponseStatus"
              }
            ]
          },
          "roles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/AccountRole"
            },
            "minItems": 0
          }
        }
      },
      "SubFamilyType": {
        "enum": [
          "valueDate",
          "chargesGeneric",
          "commissions",
          "interestsGeneric",
          "other",
          "accountClosing",
          "notAvailable",
          "sweeping",
          "topping",
          "zeroBalancing",
          "cashWithdrawal",
          "debitCardPayment",
          "crossBorderCashWithdrawal",
          "cashDeposit",
          "debitAdjustmentGeneric",
          "travellersChequesDeposit",
          "settlementAtMaturity",
          "intraCompanyTransfer",
          "corporateOwnAccountTransfer",
          "crossBorderIntraCompanyTransfer",
          "achDebit",
          "achReturn",
          "achTransactionAtxn",
          "automaticTransfer",
          "bankCheque",
          "booked",
          "domesticCreditTransfer",
          "dividend",
          "sepaCreditTransfer",
          "financialInstitutionCreditTransfer",
          "principalPayment",
          "priorityCreditTransfer",
          "reversalDueToPaymentReturn",
          "achTransactionSala",
          "sameDayValueCreditTransfer",
          "standingOrder",
          "taxes",
          "creditTransferWithAgreedCommercialInformation",
          "crossBorderCreditTransfer",
          "cashLetter",
          "cheques",
          "chequesReversal",
          "openCheque",
          "unpaidCheque",
          "crossBorderCheque",
          "sepaCoreDirectDebit",
          "directDebitPayment",
          "reversalDueToPayment",
          "reversalDueToPaymentCancellationRequest",
          "reversalDueToReturnUnpaidDirectDebit",
          "debit",
          "deposit",
          "adjustments",
          "fees",
          "creditCardPayment",
          "pointOfSalePosPayment",
          "creditAdjustment",
          "settlementAfterCollection"
        ],
        "type": "string"
      },
      "Transaction": {
        "description": "Transaction: any posting on an account",
        "required": [
          "transactionIdentifier",
          "amount",
          "currency",
          "creditDebitIndicator",
          "status",
          "transactionCode",
          "bookingDate",
          "valueDate"
        ],
        "type": "object",
        "properties": {
          "transactionIdentifier": {
            "description": "Transaction Identifier: The identifier for the transaction",
            "type": "string",
            "minLength": 0,
            "maxLength": 35
          },
          "references": {
            "type": "array",
            "items": {
              "description": "Transaction reference: unique reference associated with the transaction",
              "allOf": [
                {
                  "$ref": "#/components/schemas/TransactionReference"
                }
              ]
            },
            "minItems": 0
          },
          "creditDebitIndicator": {
            "description": "Credit is positive balance debited is negative balance",
            "allOf": [
              {
                "$ref": "#/components/schemas/CreditOrDebit"
              }
            ]
          },
          "reversalIndicator": {
            "description": "Corrected transaction indicator: Indicates whether the transaction is a correction of a previous transaction",
            "allOf": [
              {
                "$ref": "#/components/schemas/TrueFalseIndicator"
              }
            ]
          },
          "status": {
            "description": "transaction status: indicates the status of the transaction",
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionStatus"
              }
            ]
          },
          "transactionCode": {
            "description": "Transaction code: contains a set of indicators to identify the type of transaction",
            "allOf": [
              {
                "$ref": "#/components/schemas/BankTransactionCode"
              }
            ]
          },
          "bookingDate": {
            "description": "Posting date: The date when the posting of the transaction is conducted by the financial institution",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISODateTime"
              }
            ]
          },
          "valueDate": {
            "description": "Interest date: date when the transaction posting is interest-bearing",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISODateTime"
              }
            ]
          },
          "counterParties": {
            "type": "array",
            "items": {
              "description": "Counterparty: another party, the party to whom a transaction is going or coming from",
              "allOf": [
                {
                  "$ref": "#/components/schemas/CounterParty"
                }
              ]
            },
            "minItems": 0
          },
          "additionalInfo": {
            "description": "'Additional information on a transaction: textual description of the contents of a transaction'",
            "type": "string",
            "minLength": 1,
            "maxLength": 500
          },
          "currencyExchange": {
            "description": "Currency conversion: conversion of an amount from one currency to another",
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyExchange"
              }
            ]
          },
          "merchant": {
            "description": "User location: the physical location of the transaction",
            "type": "string",
            "minLength": 1,
            "maxLength": 140
          },
          "paymentCard": {
            "description": "Payment Cards: The common term for various types of cards used for cash withdrawals and for the payment of goods and services at different point of sales",
            "allOf": [
              {
                "$ref": "#/components/schemas/PaymentCard"
              }
            ]
          },
          "registered": {
            "description": "registration date: date and time when transaction was made",
            "allOf": [
              {
                "$ref": "#/components/schemas/ISODateTime"
              }
            ]
          },
          "amount": {
            "$ref": "#/components/schemas/Amount"
          },
          "currency": {
            "$ref": "#/components/schemas/CurrencyCode"
          }
        }
      },
      "TransactionReference": {
        "required": [
          "value",
          "type"
        ],
        "type": "object",
        "properties": {
          "value": {
            "type": "string"
          },
          "type": {
            "$ref": "#/components/schemas/TransactionReferenceType"
          }
        }
      },
      "TransactionReferenceType": {
        "enum": [
          "accountServicerReference",
          "archiveReference",
          "chequeNumber",
          "endToEndIdentification",
          "instructionIdentification",
          "invoiceNumber",
          "mandateIdentification",
          "messageIdentification",
          "otherReference",
          "paymentInformationIdentification",
          "remittanceReference"
        ],
        "type": "string"
      },
      "TransactionStatus": {
        "enum": [
          "booked",
          "pending",
          "info"
        ],
        "type": "string"
      },
      "Transactions": {
        "description": "Root element for response",
        "type": "object",
        "properties": {
          "responseStatus": {
            "description": "Indicates whether this is a complete response or whether there are also offline data that cannot be retrieved through the api.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ResponseStatus"
              }
            ]
          },
          "transactions": {
            "type": "array",
            "items": {
              "description": "transaction: any posting on account",
              "allOf": [
                {
                  "$ref": "#/components/schemas/Transaction"
                }
              ]
            },
            "minItems": 0
          },
          "links": {
            "type": "array",
            "items": {
              "description": "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. ",
              "allOf": [
                {
                  "$ref": "#/components/schemas/Link"
                }
              ]
            },
            "minItems": 0
          }
        },
        "xml": {
          "name": "transactions"
        }
      },
      "TrueFalseIndicator": {
        "type": "boolean"
      },
      "Error400": {
        "description": "Error structure for error message 400",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-001"
          },
          "message": {
            "type": "string",
            "description": "description of the error event that has occurred",
            "example": "Bad request. Invalid request parameters"
          }
        }
      },
      "Error401": {
        "description": "Error structure for error message 401",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-010"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Unauthorized. The request is missing authentication information"
          }
        }
      },
      "Error403": {
        "description": "Error structure for error message 403",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-011"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Forbidden. The user is not authorized for the requested service"
          }
        }
      },
      "Error404": {
        "description": "Error structure for error message 404",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-002"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Resource not found. There is no information on the requested account."
          }
        }
      },
      "Error405": {
        "description": "Error structure for error message 405",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-012"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Method not allowed. Invalid HTTP method, only GET is supported"
          }
        }
      },
      "Error429": {
        "description": "Error structure for error message 429",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-022"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Too many requests. Too many requests can be made if one chooses to impose rate-limiting services to limit the number of calls from a client."
          }
        }
      },
      "Error500": {
        "description": "Error structure for error message 500",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-100"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Internal server error. Various technical errors with the service providers."
          }
        }
      },
      "Error": {
        "description": "Error structure for all error messages",
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "error code, for automatic handling",
            "example": "ACC-0xx"
          },
          "message": {
            "type": "string",
            "description": "description of the error that has occurred",
            "example": "Informative error message"
          }
        }
      }
    }
  },
  "security": [
    {
      "accountsAuth": []
    }
  ]
}
"""
