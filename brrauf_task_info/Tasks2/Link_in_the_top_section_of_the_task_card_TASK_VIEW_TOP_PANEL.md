---
title: "Link in the top section of the task card TASK_VIEW_TOP_PANEL | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/widgets/task/view-top-panel.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/scopes/permissions.html)

You can add your item in the right panel of the old task detail form.

Starting from version `tasks 25.700.0`, a [new task card](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/tasks/tasks-new.html) has been released. The location of the `TASK_VIEW_TOP_PANEL` item is no longer present in the new card. All widgets within the card are displayed in a single Applications block.

Previously registered `TASK_VIEW_TOP_PANEL` items continue to function and are displayed in the Applications block.

![Embedded applications](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/task/_images/widget.png)

The specific widget placement code is specified in the `PLACEMENT` parameter of the [placement.bind](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/placement-bind.html) method.

The widget will not be displayed in the interface until the application installation is complete. [Check the application installation](https://apidocs.bitrix24.com/api-reference/widgets/task/settings/app-installation/installation-finish.html)

## Where the widget is embedded

| **Widget code** | **Location** |
| --- | --- |
| `TASK_VIEW_TOP_PANEL` | Item in the top section of the task card |

## What the handler receives

Data is sent as a POST request

```php
Array
(
    [DOMAIN] => xxx.bitrix24.com
    [PROTOCOL] => 1
    [LANG] => en
    [APP_SID] => dac3aa71afd1a1fd8bef05a282dd0b20
    [AUTH_ID] => 3153ba6600705a0700005a4b00000001f0f107fd2c2625abb62bad95fe9b37a0d1fbb6
    [AUTH_EXPIRES] => 3600
    [REFRESH_ID] => 21d2e16600705a0700005a4b00000001f0f10707ca46d62b79fcd8d19a8c614e621226
    [member_id] => da45a03b265edd8787f8a258d793cc5d
    [status] => L
    [PLACEMENT] => TASK_VIEW_TOP_PANEL
    [PLACEMENT_OPTIONS] => {"TASK_ID":"286"}
)
```

Required parameters are marked with \*

| **Parameter**   `type` | **Description** |
| --- | --- |
| **DOMAIN** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | The Bitrix24 address where the widget handler was invoked |
| **PROTOCOL** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Secure or non-secure HTTP protocol:  - `0` - HTTP - `1` - HTTPS |
| **LANG** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | The user interface language of Bitrix24 that invoked the widget. You can localize the interface language in your widget based on this value |
| **APP\_SID**   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | String identifier of the application that registered the widget handler |
| **AUTH\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Authorization token [OAuth 2](https://apidocs.bitrix24.com/api-reference/widgets/task/settings/oauth/simple-way.html) issued for the user who invoked the widget. Can be used for REST API calls on behalf of this user |
| **AUTH\_EXPIRES**   [`integer`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Time in seconds after which the authorization token will become invalid |
| **REFRESH\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Refresh token [OAuth 2](https://apidocs.bitrix24.com/api-reference/widgets/task/settings/oauth/simple-way.html) issued for the user who invoked the widget. Can be used to refresh the authorization token on behalf of this user |
| **member\_id** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Unique string identifier of Bitrix24 where the widget handler was invoked. |
| **status**   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Type of application that registered the handler for this widget. Accepts values:  - `L` - [local](https://apidocs.bitrix24.com/api-reference/widgets/task/local-integrations/local-apps.html) application - `F` - [free mass-market](https://apidocs.bitrix24.com/api-reference/widgets/task/market/index.html) application |
| **PLACEMENT** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Code for the widget embedding location. You can use the same handler URL for all your widgets. The value that Bitrix24 will report in the `PLACEMENT` parameter will help determine from which specific widget embedding location your handler was invoked in each case |
| **PLACEMENT\_OPTIONS**   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | Additional data in the form of a JSON string that defines the context of the widget execution. For example, this could be an array containing the numeric identifier of the CRM entity in the detail form where the widget handler was invoked, etc. The `PLACEMENT_OPTIONS` parameter, along with the `PLACEMENT` parameter, allows you to accurately determine for which specific widget embedding location and object the widget handler was invoked. |

### PLACEMENT\_OPTIONS

The value of `PLACEMENT_OPTIONS` is a JSON string containing an array of one or more keys.

Required parameters are marked with \*

| **Parameter** | **Description** |
| --- | --- |
| **TASK\_ID** \*   [`string`](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/data-types.html) | The identifier of the task for which the widget was opened.  It can be used to retrieve additional information using the [tasks.task.get](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/tasks/tasks-task-get.html) method. |

## Continue exploring

- [Install Widget Handler placement.bind](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/placement-bind.html)
- [Interaction with UI from Widgets](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/ui-interaction/index.html)
- [Interaction with CRM Card](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/ui-interaction/crm-card.html)
- [Interactive Applications](https://apidocs.bitrix24.com/api-reference/widgets/task/settings/interactivity/index.html)
- [Open a Slider with Your Interface](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/open-application.html)
- [Open Standard Bitrix24 Pages from Application Widgets](https://apidocs.bitrix24.com/api-reference/widgets/task/api-reference/widgets/open-path.html)