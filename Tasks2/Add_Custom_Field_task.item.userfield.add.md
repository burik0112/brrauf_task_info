---
title: "Add Custom Field task.item.userfield.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-add.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
We are still updating this page

Some data may be missing here — we will fill it in shortly

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/scopes/permissions.html)
> 
> Who can execute the method: administrator

The method `task.item.userfield.add` creates a new property.

When creating a custom field, the field name `FIELD_NAME` must use the prefix `UF_`. If the prefix is not specified, the system will automatically add it to the beginning of the name.

## Parameters

| **Parameter** / **Type** | **Description** |
| --- | --- |
| **auth**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Authorization token. |
| **PARAMS**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | An array with property parameters of the form `array("parameter": 'value' [, ...])`, containing the following parameters:  - `USER_TYPE_ID` - data type of the custom field. Allowed values: 	- `string` — string 	- `double` — number 	- `date` — date 	- `boolean` — yes/no - `FIELD_NAME` - field code; - `XML_ID` - external code; - `EDIT_FORM_LABEL` - label in the formatting form (specified in English ('en') and German ('de') languages); - `LABEL` - field title. |

## Examples

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST "https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.userfield.add" \
    -H "Content-Type: application/json" \
    -d '{
        "PARAMS": {
            "USER_TYPE_ID": "string",
            "FIELD_NAME": "NEW_TASKS_FIELD",
            "XML_ID": "MY_TASK_FIELD",
            "EDIT_FORM_LABEL": {
                "en": "New task field",
                "de": "Neues Aufgabenfeld"
            },
            "LABEL": "New task field"
        },
        "auth": "**put_access_token_here**"
    }'
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.userfield.add',
        {
            PARAMS:
            {
                'USER_TYPE_ID' : 'string',
                'FIELD_NAME' : 'NEW_TASKS_FIELD',
                'XML_ID' : 'MY_TASK_FIELD',
                'EDIT_FORM_LABEL' : {'en':'New task field', 'de':'Neues Aufgabenfeld'},
                'LABEL' : 'New task field'
            }
        }
    );
    
    const result = response.getData().result;
    console.info(result);
    console.log(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.item.userfield.add',
            [
                'PARAMS' => [
                    'USER_TYPE_ID'    => 'string',
                    'FIELD_NAME'      => 'NEW_TASKS_FIELD',
                    'XML_ID'          => 'MY_TASK_FIELD',
                    'EDIT_FORM_LABEL' => ['en' => 'New task field', 'de' => 'Neues Aufgabenfeld'],
                    'LABEL'           => 'New task field',
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error adding user field: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.userfield.add',
    {
        PARAMS:
        {
            'USER_TYPE_ID' : 'string',
            'FIELD_NAME' : 'NEW_TASKS_FIELD',
            'XML_ID' : 'MY_TASK_FIELD',
            'EDIT_FORM_LABEL' : {'en':'New task field', 'de':'Neues Aufgabenfeld'},
            'LABEL' : 'New task field'
        }
    },
    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.item.userfield.add',
    [
        'PARAMS' => [
            'USER_TYPE_ID' => 'string',
            'FIELD_NAME' => 'NEW_TASKS_FIELD',
            'XML_ID' => 'MY_TASK_FIELD',
            'EDIT_FORM_LABEL' => [
                'en' => 'New task field',
                'de' => 'Neues Aufgabenfeld',
            ],
            'LABEL' => 'New task field',
        ],
    ]
);

echo '<pre>';
print_r($result);
echo '</pre>';
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)