## Customers - `/customers/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  Anonymous |  `/customers/` | `GET`|  `json` |  `200` |
|  Anonymous |  `/customers/:id` | `GET`|  `json` |  `200`, `404` |
	


### DETAIL
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

- Add the customer id to the URL: /customers/:id/

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  user id |
|  `email`|  email | user email |
|  `address` | datetime  |  user address |

#### Example

**Event**: Anonymous `GET` to `/customers/1/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: `None`
```
```
**HTTP Status Code**: `200`  
**Response Content**:
```
{
    "id": 1,
    "email": "mail@gmail.com",
    "address": "Moutain View, 33"
}
```

### LIST
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

- None

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  user id |
|  `email`|  email | user email |
|  `address` | datetime  |  user address |

#### Example

**Event**: Anonymous `GET` to `/customers/`
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: `None`
```
```
**HTTP Status Code**: `200`  
**Response Content**:
```
[
  {
    "id": 1,
    "email": "mail@gmail.com",
    "address": "Moutain View, 33"
  },
  {
    "id": 2,
    "email": "mail@gmail.com",
    "address": "Moutain View, 33"
  }
]
```