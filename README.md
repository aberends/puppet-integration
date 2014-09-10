puppet-integration
===========

Integration of low level puppet modules with YAML
configuration.

In this repository, we keep construct profiles and roles to
fill in the configuration details of the Puppet modules. The
roles implement 1 or more profiles. A role can be
provisioned on a target node.

In the Puppet construction layer, we focus on writing elementary Puppet modules. So, providing the mechanism to make something work. See for a full explanation on [msat.disruptivefoss.org](http://msat.disruptivefoss.org/). In the puppet-integration repo and corresponding layer, Puppet integration, we tie together the parameters coming from YAML files to the elementary Puppet modules from the Puppet construction layer.

