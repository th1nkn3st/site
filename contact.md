---
layout: default
title: Contact
permalink: /contact/
---
{% include sorted-apps.html %}

# Contact

For questions, bug reports, or feedback about any Th1nkN3st game or app, email
[{{ site.email }}](mailto:{{ site.email }}).

When reporting a bug, please include the app name, the version, and your device model.

## App support and privacy

{% for slug in live_app_slugs %}
- **{{ site.data.apps[slug].name }}:** [support]({{ '/' | append: slug | append: '/support/' | relative_url }}) · [privacy policy]({{ '/' | append: slug | append: '/privacy/' | relative_url }})
{%- endfor %}
