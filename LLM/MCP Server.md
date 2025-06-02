Modal Context Protocol is a standard to integrate **third-party tools**, **data sources**, and **APIs** with LLMs.

MCP is like **an API app store for LLMs and agents** — plug, play, and go.  

This helps individual contributors to:
- Eliminate glue code.
- Enable modularity.
- Support agent ecosystems.

You can think of it like this — for example, you want to create a **Travel Planning Agent**. Let’s say you’d like to go to **Singapore**.

Basically MCP is a way to integrate with other Tools APIs. For example Airbnb Api, Booking. Com, Accuweather APIs. 

The agent first interacts with a **weather API**. If it finds the weather is good for a vacation, it then goes to a **flights API** for price searches, and then to a **hotel booking API**.

Once it finds that flights and hotels are available on the same day, it proceeds with the booking.

Then, it sends the details to your **email**, and also adds a **calendar invite**.

To achieve all of this, you normally need to manage auth, input/output schemas, and formatting.

With MCP, you can **streamline these efforts** and operate under a consistent protocol.

Below is the List of Awesome MCP Servers.
https://github.com/wong2/awesome-mcp-servers?tab=readme-ov-file
---