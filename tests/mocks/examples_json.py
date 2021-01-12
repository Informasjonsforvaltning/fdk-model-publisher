"""Example JSON input."""

ex_1_json = """
{
   "openapi":"3.0.0",
   "components":{
      "securitySchemes":{
         "accountsAuth":{
            "type":"http",
            "scheme":"bearer",
            "bearerFormat":"Access token (JWT)"
         }
      },
      "schemas":{
         "Eiendom":{
            "properties":{
               "erstatter":{
                  "type":"string"
               },
               "erstattetav":{
                  "type":"string"
               },
               "id":{
                  "type":"string"
               },
               "nummer":{
                  "type":"string"
               },
               "type":{
                  "type":"string"
               }
            },
            "required":[
               "id",
               "nummer",
               "type"
            ],
            "type":"object"
         }
      }
   }
}
"""

ex_2_json = """
{
   "openapi":"3.0.0",
   "components":{
      "securitySchemes":{
         "accountsAuth":{
            "type":"http",
            "scheme":"bearer",
            "bearerFormat":"Access token (JWT)"
         }
      },
      "schemas":{
         "EiendomResultat": {
                "properties": {
                    "code": {
                        "format": "int32",
                        "type": "integer"
                    },
                    "data": {
                        "$ref": "#/components/schemas/Eiendom",
                        "required": [
                            "kommune"
                        ],
                        "type": "object"
                    },
                    "message": {
                        "type": "string"
                    }
                },
                "required": [
                    "code",
                    "data",
                    "message"
                ],
                "type": "object"
            }
      }
   }
}
"""
