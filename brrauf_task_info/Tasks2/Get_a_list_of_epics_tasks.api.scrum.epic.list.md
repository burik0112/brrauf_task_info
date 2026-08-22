---
title: "Get a list of epics tasks.api.scrum.epic.list | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns a list of epics.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **order**   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | An array for sorting the result in the format `{'sorting_field': 'sorting_direction' [, ...]}`.  Sorting direction can take the following values:  - `asc` — ascending - `desc` — descending  Possible values for the array elements correspond to the fields in the response of [tasks.api.scrum.epic.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-add.html#fields) |
| **filter**   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | An array in the format `{'filter_field': 'filter_value' [, ...]}`.  The key can have an additional prefix that specifies the filter behavior.  Possible prefix values:  - `=` — equals (works with arrays as well) - `%` — LIKE, substring search. The % symbol in the filter value does not need to be passed. The search looks for the substring in any position of the string - `>` — greater than - `<` — less than - `!=` — not equal - `!%` — NOT LIKE, substring search. The % symbol in the filter value does not need to be passed. The search goes from both sides. - `>=` — greater than or equal to - `<=` — less than or equal to - `=%` — LIKE, substring search. The % symbol needs to be passed in the value. Examples: 	- `"mol%"` — searching for values starting with "mol" 	- `"%mol"` — searching for values ending with "mol" 	- `"%mol%"` — searching for values where "mol" can be in any position - `%=` — LIKE (see description above) - `!=%` — NOT LIKE, substring search. The % symbol needs to be passed in the value. Examples: 	- `"mol%"` — searching for values not starting with "mol" 	- `"%mol"` — searching for values not ending with "mol" 	- `"%mol%"` — searching for values where the substring "mol" is not present in any position - `!%=` — NOT LIKE (see description above)  Possible values for the array elements correspond to the fields in the response of [tasks.api.scrum.epic.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-add.html#fields) |
| **select**   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | An array of record fields that will be returned by the method.  Possible values for the array elements correspond to the fields in the response of [tasks.api.scrum.epic.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-add.html#fields). You can specify only the fields that are necessary.  If the array contains the value `"*"`, all available fields will be returned.  The default value is an empty array `array()`. This means that all fields from the main query table will be returned |
| **start**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | The page number of the output. Works for HTTPS requests.  The page size of results is always static: 50 records.  To select the second page of results, you need to pass the value `50`. To select the third page of results, the value is `100`, and so on.  The formula for calculating the `start` parameter value:   `start = (N-1) * 50`, where `N` is the desired page number |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "filter": {
        "GROUP_ID": 143,
        ">=ID": 1,
        "<=ID": 50,
        "NAME": "%epic%",
        "!=DESCRIPTION": "old epic"
    },
    "order": {
        "ID": "asc",
        "NAME": "desc"
    },
    "select": ["ID", "NAME", "DESCRIPTION", "CREATED_BY", "MODIFIED_BY", "COLOR"],
    "start": 0
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.api.scrum.epic.list
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
    "filter": {
        "GROUP_ID": 143,
        ">=ID": 1,
        "<=ID": 50,
        "NAME": "%epic%",
        "!=DESCRIPTION": "old epic",
        "CREATED_BY": 1,
        "MODIFIED_BY": 3,
        "COLOR": "#69dafc"
    },
    "order": {
        "ID": "asc",
        "NAME": "desc"
    },
    "select": ["ID", "NAME", "DESCRIPTION", "CREATED_BY", "MODIFIED_BY", "COLOR"],
    "start": 0,
    "auth": "YOUR_ACCESS_TOKEN"
}' \
https://your-domain.bitrix24.com/rest/tasks.api.scrum.epic.list
```

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

const groupId = 143;
try {
  const response = await $b24.callListMethod(
    'tasks.api.scrum.epic.list',
    {
      filter: {
        GROUP_ID: groupId,
        '>=ID': 1,
        '<=ID': 50,
        'NAME': '%epic%',
        '!=DESCRIPTION': 'old epic',
        'CREATED_BY': 1,
        'MODIFIED_BY': 3,
        'COLOR': '#69dafc'
      },
      order: {
        'ID': 'asc',
        'NAME': 'desc'
      },
      select: ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
      start: 0
    },
    (progress) => { console.log('Progress:', progress) }
  );
  const items = response.getData() || [];
  for (const entity of items) { console.log('Entity:', entity); }
} catch (error) {
  console.error('Request failed', error);
}

// fetchListMethod is preferred when working with large datasets. The method implements iterative fetching using a generator, allowing data to be processed in parts and efficiently using memory.

const groupId = 143;
try {
  const generator = $b24.fetchListMethod('tasks.api.scrum.epic.list', {
    filter: {
      GROUP_ID: groupId,
      '>=ID': 1,
      '<=ID': 50,
      'NAME': '%epic%',
      '!=DESCRIPTION': 'old epic',
      'CREATED_BY': 1,
      'MODIFIED_BY': 3,
      'COLOR': '#69dafc'
    },
    order: {
      'ID': 'asc',
      'NAME': 'desc'
    },
    select: ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
    start: 0
  }, 'ID');
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity); }
  }
} catch (error) {
  console.error('Request failed', error);
}

// callMethod provides manual control over the pagination process through the start parameter. Suitable for scenarios where precise control over request batches is required. However, with large volumes of data, it may be less efficient compared to fetchListMethod.

const groupId = 143;
try {
  const response = await $b24.callMethod('tasks.api.scrum.epic.list', {
    filter: {
      GROUP_ID: groupId,
      '>=ID': 1,
      '<=ID': 50,
      'NAME': '%epic%',
      '!=DESCRIPTION': 'old epic',
      'CREATED_BY': 1,
      'MODIFIED_BY': 3,
      'COLOR': '#69dafc'
    },
    order: {
      'ID': 'asc',
      'NAME': 'desc'
    },
    select: ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
    start: 0
  }, 0);
  const result = response.getData().result || [];
  for (const entity of result) { console.log('Entity:', entity); }
} catch (error) {
  console.error('Request failed', error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.epic.list',
            [
                'filter' => [
                    'GROUP_ID'      => $groupId,
                    '>=ID'          => 1,
                    '<=ID'          => 50,
                    'NAME'          => '%epic%',
                    '!=DESCRIPTION' => 'old epic',
                    'CREATED_BY'    => 1,
                    'MODIFIED_BY'   => 3,
                    'COLOR'         => '#69dafc'
                ],
                'order'  => [
                    'ID'   => 'asc',
                    'NAME' => 'desc'
                ],
                'select' => ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
                'start'  => 0
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error: ' . $e->getMessage();
}
```

```js
const groupId = 143;
BX24.callMethod(
    'tasks.api.scrum.epic.list',
    {
        filter: {
            GROUP_ID: groupId,
            '>=ID': 1,
            '<=ID': 50,
            'NAME': '%epic%',
            '!=DESCRIPTION': 'old epic',
            'CREATED_BY': 1,
            'MODIFIED_BY': 3,
            'COLOR': '#69dafc'
        },
        order: {
            'ID': 'asc',
            'NAME': 'desc'
        },
        select: ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
        start: 0
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php'); // include CRest PHP SDK

// execute a request to the REST API
$result = CRest::call(
    'tasks.api.scrum.epic.list',
    [
        'filter' => [
            'GROUP_ID' => 143,
            '>=ID' => 1,
            '<=ID' => 50,
            'NAME' => '%epic%',
            '!=DESCRIPTION' => 'old epic',
            'CREATED_BY' => 1,
            'MODIFIED_BY' => 3,
            'COLOR' => '#69dafc'
        ],
        'order' => [
            'ID' => 'asc',
            'NAME' => 'desc'
        ],
        'select' => ['ID', 'NAME', 'DESCRIPTION', 'CREATED_BY', 'MODIFIED_BY', 'COLOR'],
        'start' => 0
    ]
);

// Processing the response from Bitrix24
if ($result['error']) {
    echo 'Error: '.$result['error_description'];
}
else {
    print_r($result['result']);
}
```

## Response Handling

HTTP status: **200**

```json
[
    {
        "id": 1,
        "groupId": 143,
        "name": "epic",
        "description": "",
        "createdBy": 1,
        "modifiedBy": 0,
        "color": "#69dafc"
    },
    {
        "id": 3,
        "groupId": 143,
        "name": "epic2",
        "description": "new epic",
        "createdBy": 3,
        "modifiedBy": 5,
        "color": "#69dagc"
    }
]
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic identifier |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Group identifier (scrum) to which the epic is linked |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic name |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic description |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who created the epic |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who last modified the epic |
| **color**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic color in HEX format |

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Could not load list"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Could not load list | No epics found with the specified filters |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue Learning

- [Epics in Scrum: Overview of Methods](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/index.html)
- [Add Epic in Scrum tasks.api.scrum.epic.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-add.html)
- [Update Epic in Scrum tasks.api.scrum.epic.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-update.html)
- [Get Epic Fields by Its Identifier tasks.api.scrum.epic.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get.html)
- [Delete Epic tasks.api.scrum.epic.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-delete.html)
- [Get a list of available fields for epic tasks.api.scrum.epic.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get-fields.html)