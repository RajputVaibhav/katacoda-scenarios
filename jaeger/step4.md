You can access the Jaeger dashboard at

https://[[HOST_SUBDOMAIN]]-16686-[[KATACODA_HOST]].environments.katacoda.com

<br/>

Once you are there, click on **Services** dropdown (If it has no content, refresh the page).

Now choose a service that you wish to trace and click **Find Trace**

<br/>

On clicking Find Trace, you can now view the metadata of the Traces, such as the time at which the trace was initiated, time it took to execute, names of different services that participated in the trace, and the number of spans (logical unit of work) each service emitted to Jaeger.

<br/>

If you click on it to open it, you get the timeline view. The timeline view shows a typical view of a trace as a time sequence of nested spans, where a span represents a unit of work within a single service.
