# 
# http://arquivoskodi.com.br

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyAgICAgIENvcHlyaWdodCAoQykgMjAxOSBkcmluZmVybm9vICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkgICAgICAgICMKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiwgb3IgKGF0IHlvdXIgb3B0aW9uKSAgICAgICAgICMKIyAgYW55IGxhdGVyIHZlcnNpb24uICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGRpc3RyaWJ1dGVkIGluIHRoZSBob3BlIHRoYXQgaXQgd2lsbCBiZSB1c2VmdWwsICAgICAgICAgICAgICMKIyAgYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YgICAgICAgICAgICAgICMKIyAgTUVSQ0hBTlRBQklMSVRZIG9yIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFLiBTZWUgdGhlICAgICAgICAgICAgICAgICMKIyAgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgZm9yIG1vcmUgZGV0YWlscy4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgWW91IHNob3VsZCBoYXZlIHJlY2VpdmVkIGEgY29weSBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgICAgICAgICAgICMKIyAgYWxvbmcgd2l0aCBYQk1DOyBzZWUgdGhlIGZpbGUgQ09QWUlORy4gIElmIG5vdCwgd3JpdGUgdG8gICAgICAgICAgICAgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbiwgNjc1IE1hc3MgQXZlLCBDYW1icmlkZ2UsIE1BIDAyMTM5LCBVU0EuICAgICAgICMKIyAgaHR0cDovL3d3dy5nbnUub3JnL2NvcHlsZWZ0L2dwbC5odG1sICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmltcG9ydCB4Ym1jCmltcG9ydCB4Ym1jZ3VpCgppbXBvcnQgb3MKCmZyb20gcmVzb3VyY2VzLmxpYnMuY29tbW9uLmNvbmZpZyBpbXBvcnQgQ09ORklHCmZyb20gcmVzb3VyY2VzLmxpYnMuY29tbW9uIGltcG9ydCBkaXJlY3RvcnkKZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IGxvZ2dpbmcKZnJvbSByZXNvdXJjZXMubGlicy5jb21tb24gaW1wb3J0IHRvb2xzCmZyb20gcmVzb3VyY2VzLmxpYnMuZ3VpIGltcG9ydCB3aW5kb3cKCgpkZWYgdmlld19jdXJyZW50KCk6CiAgICB3aW5kb3cuc2hvd190ZXh0X2JveChDT05GSUcuQURET05USVRMRSwgdG9vbHMucmVhZF9mcm9tX2ZpbGUoQ09ORklHLkFEVkFOQ0VEKS5yZXBsYWNlKCdcdCcsICcgICAgJykpCgoKZGVmIHJlbW92ZV9jdXJyZW50KCk6CiAgICBkaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpCiAgICBvayA9IGRpYWxvZy55ZXNubyhDT05GSUcuQURET05USVRMRSwgIltDT0xPUiB7MH1dVGVtIGNlcnRlemEgZGUgcXVlIGRlc2VqYSByZW1vdmVyIG8gYWR2YW5jZWRzZXR0aW5ncy54bWwgYXR1YWw/Wy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IyKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHllc2xhYmVsPSJbQl1bQ09MT1Igc3ByaW5nZ3JlZW5dU2ltWy9DT0xPUl1bL0JdIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5vbGFiZWw9IltCXVtDT0xPUiByZWRdTsOjb1svQ09MT1JdWy9CXSIpCgogICAgaWYgb2s6CiAgICAgICAgaWYgb3MucGF0aC5leGlzdHMoQ09ORklHLkFEVkFOQ0VEKToKICAgICAgICAgICAgdG9vbHMucmVtb3ZlX2ZpbGUoQ09ORklHLkFEVkFOQ0VEKQogICAgICAgICAgICBsb2dnaW5nLmxvZ19ub3RpZnkoIltDT0xPUiB7MH1dezF9Wy9DT0xPUl0iLmZvcm1hdChDT05GSUcuQ09MT1IxLCBDT05GSUcuQURET05USVRMRSksCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiW0NPTE9SIHswfV1hZHZhbmNlZHNldHRpbmdzLnhtbCByZW1vdmlkb1svQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMikpCiAgICAgICAgICAgIHhibWMuZXhlY3V0ZWJ1aWx0aW4oJ0NvbnRhaW5lci5SZWZyZXNoKCknKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGxvZ2dpbmcubG9nX25vdGlmeSgiW0NPTE9SIHswfV17MX1bL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjEsIENPTkZJRy5BRERPTlRJVExFKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJbQ09MT1IgezB9XWFkdmFuY2Vkc2V0dGluZ3MueG1sIG7Do28gZW5jb250cmFkb1svQ09MT1JdIi5mb3JtYXQoQ09ORklHLkNPTE9SMikpCiAgICBlbHNlOgogICAgICAgIGxvZ2dpbmcubG9nX25vdGlmeSgiW0NPTE9SIHswfV17MX1bL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjEsIENPTkZJRy5BRERPTlRJVExFKSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJbQ09MT1IgezB9XWFkdmFuY2Vkc2V0dGluZ3MueG1sIG7Do28gcmVtb3ZpZG9bL0NPTE9SXSIuZm9ybWF0KENPTkZJRy5DT0xPUjIpKQoKCmRlZiBfd3JpdGVfc2V0dGluZyhjYXRlZ29yeSwgdGFnLCB2YWx1ZSk6CiAgICBmcm9tIHhtbC5ldHJlZSBpbXBvcnQgRWxlbWVudFRyZWUKCiAgICBleGlzdHMgPSBvcy5wYXRoLmV4aXN0cyhDT05GSUcuQURWQU5DRUQpCgogICAgaWYgZXhpc3RzOgogICAgICAgIHJvb3QgPSBFbGVtZW50VHJlZS5wYXJzZShDT05GSUcuQURWQU5DRUQpLmdldHJvb3QoKQogICAgZWxzZToKICAgICAgICByb290ID0gRWxlbWVudFRyZWUuRWxlbWVudCgnYWR2YW5jZWRzZXR0aW5ncycpCgogICAgdHJlZV9jYXRlZ29yeSA9IHJvb3QuZmluZCgnLi97MH0nLmZvcm1hdChjYXRlZ29yeSkpCiAgICBpZiB0cmVlX2NhdGVnb3J5IGlzIE5vbmU6CiAgICAgICAgdHJlZV9jYXRlZ29yeSA9IEVsZW1lbnRUcmVlLlN1YkVsZW1lbnQocm9vdCwgY2F0ZWdvcnkpCgogICAgY2F0ZWdvcnlfdGFnID0gdHJlZV9jYXRlZ29yeS5maW5kKHRhZykKICAgIGlmIGNhdGVnb3J5X3RhZyBpcyBOb25lOgogICAgICAgIGNhdGVnb3J5X3RhZyA9IEVsZW1lbnRUcmVlLlN1YkVsZW1lbnQodHJlZV9jYXRlZ29yeSwgdGFnKQoKICAgIGNhdGVnb3J5X3RhZy50ZXh0ID0gJ3swfScuZm9ybWF0KHZhbHVlKQoKICAgIHRyZWUgPSBFbGVtZW50VHJlZS5FbGVtZW50VHJlZShyb290KQoKICAgIGxvZ2dpbmcubG9nKCdFc2NyZXZlbmRvIHswfSAtIHsxfTogez'
love = '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'
god = 'XSBVUkwgbm90IHdvcmtpbmc6IHswfSIuZm9ybWF0KENPTkZJRy5BRFZBTkNFREZJTEUpKQoKICAgIGRlZiBxdWlja19jb25maWd1cmUoc2VsZik6CiAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKCdBcyBhbHRlcmHDp8O1ZXMgbsOjbyBzZXLDo28gcmVmbGV0aWRhcyBhdMOpIHF1ZSBvIEtvZGkgc2VqYSByZWluaWNpYWRvLicsIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnQ2xpcXVlIGFxdWkgcGFyYSByZWluaWNpYXIgbyBLb2RpLicsIHsnbW9kZSc6ICdmb3JjZWNsb3NlJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQogICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnTWFpcyBjYXRlZ29yaWFzIGVtIGJyZXZlIDopJywgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpCiAgICAgICAgZGlyZWN0b3J5LmFkZF9zZXBhcmF0b3IobWlkZGxlPSdDQVRFR09SSUVTJykKICAgICAgICAjIGRpcmVjdG9yeS5hZGRfZGlyKCdUcm91Ymxlc2hvb3RpbmcnLCB7J21vZGUnOiAnYWR2YW5jZWRfc2V0dGluZ3MnLCAnYWN0aW9uJzogJ3Nob3dfc2VjdGlvbicsICd0YWdzJzogJ2xvZ2xldmVsfGpzb25ycGMnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpCiAgICAgICAgIyBkaXJlY3RvcnkuYWRkX2RpcignUGxheWJhY2snLCB7J21vZGUnOiAnYWR2YW5jZWRfc2V0dGluZ3MnLCAnYWN0aW9uJzogJ3Nob3dfc2VjdGlvbicsICd0YWdzJzogJ3NraXBsb29wZmlsdGVyfHZpZGVvfGF1ZGlvfGVkbHxwdnJ8ZXBnfGZvcmNlZHN3YXB0aW1lJ30sIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQogICAgICAgICMgZGlyZWN0b3J5LmFkZF9kaXIoJ1ZpZGVvIExpYnJhcnknLCB7J21vZGUnOiAnYWR2YW5jZWRfc2V0dGluZ3MnLCAnYWN0aW9uJzogJ3Nob3dfc2VjdGlvbicsICd0YWdzJzogJ3ZpZGVvZXh0ZW5zaW9uc3xkaXNjc3R1YmV4dGVuc2lvbnN8bGFuZ3VhZ2Vjb2Rlc3xtb3ZpZXN0YWNraW5nfGZvbGRlcnN0YWNraW5nfGNsZWFuZGF0ZXRpbWV8Y2xlYW5zdHJpbmdzfHR2c2hvd21hdGNoaW5nfHR2bXVsdGlwYXJ0bWF0Y2hpbmcnfSwgaWNvbj1DT05GSUcuSUNPTk1BSU5ULCB0aGVtZWl0PUNPTkZJRy5USEVNRTMpCiAgICAgICAgZGlyZWN0b3J5LmFkZF9kaXIoJ1JlZGUgZSBDYWNoZScsIHsnbW9kZSc6ICdhZHZhbmNlZF9zZXR0aW5ncycsICdhY3Rpb24nOiAnc2hvd19zZWN0aW9uJywgJ3RhZ3MnOiAnY2FjaGV8bmV0d29yayd9LCBpY29uPUNPTkZJRy5JQ09OTUFJTlQsIHRoZW1laXQ9Q09ORklHLlRIRU1FMykKCiAgICBkZWYgc2hvd19zZWN0aW9uKHNlbGYsIHRhZ3MpOgogICAgICAgIGZyb20geG1sLmV0cmVlIGltcG9ydCBFbGVtZW50VHJlZQoKICAgICAgICBzcGxpdF90YWdzID0gdGFncy5zcGxpdCgnfCcpCiAgICAgICAgbG9nZ2luZy5sb2coc3BsaXRfdGFncykKCiAgICAgICAgZXhpc3RzID0gb3MucGF0aC5leGlzdHMoQ09ORklHLkFEVkFOQ0VEKQoKICAgICAgICBpZiBleGlzdHM6CiAgICAgICAgICAgIHJvb3QgPSBFbGVtZW50VHJlZS5wYXJzZShDT05GSUcuQURWQU5DRUQpLmdldHJvb3QoKQoKICAgICAgICAgICAgZm9yIGNhdGVnb3J5IGluIHJvb3QuZmluZGFsbCgnKicpOgogICAgICAgICAgICAgICAgbmFtZSA9IGNhdGVnb3J5LnRhZwogICAgICAgICAgICAgICAgaWYgbmFtZSBub3QgaW4gc3BsaXRfdGFnczoKICAgICAgICAgICAgICAgICAgICBjb250aW51ZQoKICAgICAgICAgICAgICAgIHZhbHVlcyA9IHt9CgogICAgICAgICAgICAgICAgZm9yIGVsZW1lbnQgaW4gY2F0ZWdvcnkuZmluZGFsbCgnKicpOgogICAgICAgICAgICAgICAgICAgIHZhbHVlc1tlbGVtZW50LnRhZ10gPSBlbGVtZW50LnRleHQKCiAgICAgICAgICAgICAgICBzZWxmLnRhZ3NbbmFtZV0gPSB2YWx1ZXMKCiAgICAgICAgaWYgbGVuKHNlbGYudGFncykgPT0gMDoKICAgICAgICAgICAgZGlyZWN0b3J5LmFkZF9maWxlKCdOZW5odW1hIGNvbmZpZ3VyYcOnw6NvIHBhcmEgZXN0YSBjYXRlZ29yaWEgZXhpc3RlIGVtIHNldSBhdHVhbCBhZHZhbmNlZHNldHRpbmdzLnhtbCBhcnF1aXZvLicsIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQogICAgICAgICAgICBkaXJlY3RvcnkuYWRkX3NlcGFyYXRvcigpCiAgICAgICAgICAgIAogICAgICAgIGZvciBjYXRlZ29yeSBpbiBzZWxmLnRhZ3M6CiAgICAgICAgICAgIGRpcmVjdG9yeS5hZGRfc2VwYXJhdG9yKGNhdGVnb3J5LnVwcGVyKCkpCgogICAgICAgICAgICBmb3IgdGFnIGluIHNlbGYudGFnc1tjYXRlZ29yeV06CiAgICAgICAgICAgICAgICB2YWx1ZSA9IHNlbGYudGFnc1tjYXRlZ29yeV1bdGFnXQoKICAgICAgICAgICAgICAgIGlmIHZhbHVlIGlzIE5vbmU6CiAgICAgICAgICAgICAgICAgICAgdmFsdWUgPSAnJwoKICAgICAgICAgICAgICAgIGRpcmVjdG9yeS5hZGRfZmlsZSgnezB9OiB7MX0nLmZvcm1hdCh0YWcsIHZhbHVlKSwgeydtb2RlJzogJ2FkdmFuY2VkX3NldHRpbmdzJywgJ2FjdGlvbic6ICdzZXRfc2V0dGluZycsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnY2F0ZWdvcnknOiBjYXRlZ29yeSwgJ3RhZyc6IHRhZywgJ3ZhbHVlJzogdmFsdWV9LAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGljb249Q09ORklHLklDT05NQUlOVCwgdGhlbWVpdD1DT05GSUcuVEhFTUUzKQoKICAgIGRlZiBzZXRfc2V0dGluZyhzZWxmLCBjYXRlZ29yeSwgdGFnLCBjdXJyZW50KToKICAgICAgICB2YWx1ZSA9IE5vbmUKICAgICAgICAKICAgICAgICBpZiBjYXRlZ29yeSA9PSAnY2FjaGUnOgogICAgICAgICAgICB2YWx1ZSA9IHNlbGYuX2NhY2hlKHRhZywgY3VycmVudCkKICAgICAgICBlbGlmIGNhdGVnb3J5ID09ICduZXR3b3JrJzoKICAgICAgICAgICAgdmFsdWUgPSBzZWxmLl9uZXR3b3JrKHRhZywgY3VycmVudCkKICAgICAgICAgICAgCiAgICAgICAgaWYgdmFsdWU6CiAgICAgICAgICAgIF93cml0ZV9zZXR0aW5nKGNhdGVnb3J5LCB0YWcsIHZhbHVlKQogICAgICAgICAgICAKICAgIGRlZiBfY2FjaGUoc2VsZiwgdGFnLCBjdXJyZW50KToKICAgICAgICB2YWx1ZSA9IE5vbmUKICAgICAgICAKICAgICAgICBpZiB0YWcgPT0gJ2J1ZmZlcm1vZGUnOgogICAgICAgICAgICB2YWx1ZXMgPSBbJ0J1ZmZlciBhbGwgaW50ZXJuZXQgZmlsZXN5c3RlbXMnLAogICAgICAgICAgICAgICAgICAgICAgJ0J1ZmZlciBhbGwgZmlsZXN5c3RlbXMnLAogICAgICAgICAgICAgICAgICAgICAgJ09ubHkgYnVmZmVyIHRydWUgaW50ZXJuZXQgZmlsZXN5c3RlbXMnLAogICAgICAgICAgICAgICAgICAgICAgJ05vIGJ1ZmZlcicsCiAgICAgICAgICAgICAgICAgICAgICAnQWxsIG5ldHdvcmsgZmlsZXN5c3RlbXMnXQogICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgIGl0ZW1zID0gW10KICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKHZhbHVlcykpOgogICAgICAgICAgICAgICAgaXRlbXMuYXBwZW5kKHhibWNndWkuTGlzdEl0ZW0obGFiZWw9c3RyKGkpLCBsYWJlbDI9dmFsdWVzW2ldKSkKICAgICAgICAgICAgICAgICAgICAgIAogIC'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))