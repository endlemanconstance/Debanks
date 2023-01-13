<?xml version="1.0" encoding="UTF-8"?>
<BrowserAutomationStudioProject>
     <Script><![CDATA[section(1 /*1*/,1 /*1*/,1 /*1*/,0,function(){
   section_start("\u007b\u0022n\u0022:\u0022Initialize\u0022\u007d", 0)!

   section_end()!

   _call(_on_start, null)!

   section_start("", 680112276)!
   /*Dat:eyJzIjoibG9hZCIsInYiOjEsImYiOltdLCJ1dyI6IjEiLCJ1dCI6IjAiLCJ1dG8iOiIwIiwidW0iOiIwIiwiZCI6W3siaWQiOiJMb2FkVXJsIiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiJodHRwczovL3RoZW1pY2Ryb3AucGVwc2kuY29tLyIsImNsYXNzIjoic3RyaW5nIn0seyJpZCI6IlJlZmVycmVyIiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiIiLCJjbGFzcyI6InN0cmluZyJ9XX0=*/
   _load("https://themicdrop.pepsi.com/", "", false)!
   section_end()!

   section_start("", 284515672)!
   /*Dat:eyJzIjoiZXhpc3QiLCJ2IjoxLCJmIjpbXSwidXciOiIwIiwidXQiOiIwIiwidXRvIjoiMCIsInVtIjoiMCIsImQiOlt7ImlkIjoiU2F2ZSIsInR5cGUiOiJ2YXIiLCJkYXRhIjoiSVNfRVhJU1RTIn0seyJpZCI6IkNoZWNrIiwidHlwZSI6ImNoZWNrIiwiZGF0YSI6ZmFsc2V9XSwicCI6eyJpc19pbWFnZSI6ZmFsc2UsImNzcyI6IiA+Q1NTPiAjbWFpbi1pZnJhbWU+RlJBTUU+ID5DU1M+IGgxIiwidmVyc2lvbiI6IjEuMCIsImNzczEiOiIgPkNTUz4gI21haW4taWZyYW1lPkZSQU1FPiA+Q1NTPiBoMSIsImNzczIiOiIgPkNTUz4gaWZyYW1lPkZSQU1FPiA+Q1NTPiBoMSIsImNzczMiOiIiLCJjdXJyZW50IjoibWF0Y2giLCJtYXRjaCI6Ij5NQVRDSD48aWZyYW1lIGlkPVwibWFpbi1pZnJhbWVcIiBzcmM9XCIvX0luY2Fwc3VsPkZSQU1FPj5NQVRDSD48aDE+dGhlbWljZHJvcC5wZXBzaS5jb20gQWRkaXRpb25hbCBzZWN1IiwieHBhdGgiOiIgPlhQQVRIPiBpZChcIm1haW4taWZyYW1lXCIpPkZSQU1FPiA+WFBBVEg+IC9odG1sWzFdL2JvZHlbMV0vZGl2W0BjbGFzcz1cImNvbnRhaW5lclwiXS9kaXZbQGNsYXNzPVwiY29udGFpbmVyLWlubmVyXCJdL2RpdltAY2xhc3M9XCJtYWluXCJdL2RpdltAY2xhc3M9XCJtYWluLWlubmVyXCJdL2RpdltAY2xhc3M9XCJlcnJvci1oZWFkbGluZVwiXS9kaXZbQGNsYXNzPVwiaGVhZGxpbmUtaW5uZXJcIl0vaDFbMV0iLCJhdCI6IjM2MiwgNTAiLCJ3ZSI6ZmFsc2UsImZhIjpmYWxzZX19*/
   /*Browser*/
   ;_SELECTOR="\u003eMATCH\u003e\u003ciframe id=\u0022main-iframe\u0022 src=\u0022/_Incapsul\u003eFRAME\u003e\u003eMATCH\u003e\u003ch1\u003ethemicdrop.pepsi.com Additional secu";
   get_element_selector(_SELECTOR, false).nowait().exist()!
   VAR_IS_EXISTS = _result() == 1
   section_end()!

   section_start("", 457769907)!
   /*Dat:eyJzIjoiaWYiLCJ2IjoxLCJmIjpbXSwidXciOiIwIiwidXQiOiIwIiwidXRvIjoiMCIsInVtIjoiMCIsImQiOlt7ImlkIjoiSWZFeHByZXNzaW9uIiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiJbW0lTX0VYSVNUU11dID09IDEiLCJjbGFzcyI6ImV4cHJlc3Npb24ifSx7ImlkIjoiSWZFbHNlIiwidHlwZSI6ImNoZWNrIiwiZGF0YSI6ZmFsc2V9XX0=*/
   _set_if_expression("W1tJU19FWElTVFNdXSA9PSAx");
   _if(VAR_IS_EXISTS == 1,function(){
   section_insert()
      section_start("", 842039307)!
      /*Dat:eyJzIjoiY2xpY2tlbGVtZW50IiwidiI6MSwiZiI6W10sInV3IjoiMCIsInV0IjoiMCIsInV0byI6IjAiLCJ1bSI6IjAiLCJkIjpbeyJpZCI6IkNoZWNrIiwidHlwZSI6ImNoZWNrIiwiZGF0YSI6ZmFsc2V9XSwicCI6eyJpc19pbWFnZSI6ZmFsc2UsImNzcyI6IiA+Q1NTPiAjbWFpbi1pZnJhbWU+RlJBTUU+ID5DU1M+IDpudGgtY2hpbGQoMSkgPiA6bnRoLWNoaWxkKDEpID4gZGl2ID4gaWZyYW1lPkZSQU1FPiA+Q1NTPiAjcmVjYXB0Y2hhLWFuY2hvciA+IDpudGgtY2hpbGQoMSkiLCJ2ZXJzaW9uIjoiMS4wIiwiY3NzMSI6IiA+Q1NTPiAjbWFpbi1pZnJhbWU+RlJBTUU+ID5DU1M+IDpudGgtY2hpbGQoMSkgPiA6bnRoLWNoaWxkKDEpID4gZGl2ID4gaWZyYW1lPkZSQU1FPiA+Q1NTPiAjcmVjYXB0Y2hhLWFuY2hvciA+IDpudGgtY2hpbGQoMSkiLCJjc3MyIjoiID5DU1M+IGlmcmFtZT5GUkFNRT4gPkNTUz4gOm50aC1jaGlsZCgxKSA+IDpudGgtY2hpbGQoMSkgPiBkaXYgPiBpZnJhbWU+RlJBTUU+ID5DU1M+IHNwYW4gPiA6bnRoLWNoaWxkKDEpIiwiY3NzMyI6IiA+Q1NTPiAjbWFpbi1pZnJhbWU+RlJBTUU+ID5DU1M+IC5nLXJlY2FwdGNoYSA+IDpudGgtY2hpbGQoMSkgPiBkaXYgPiBpZnJhbWU+RlJBTUU+ID5DU1M+IC5yZWNhcHRjaGEtY2hlY2tib3gtYm9yZGVyIiwiY3VycmVudCI6ImNzcyIsIm1hdGNoIjoiPk1BVENIPjxpZnJhbWUgaWQ9XCJtYWluLWlmcmFtZVwiIHNyYz1cIi9fSW5jYXBzdWw+RlJBTUU+Pk1BVENIPjxpZnJhbWUgdGl0bGU9XCJyZUNBUFRDSEFcIiBzcmM9XCJodHRwczovL3c+RlJBTUU+Pk1BVENIPjxkaXYgY2xhc3M9XCJyZWNhcHRjaGEtY2hlY2tib3gtYm9yZGVyXCIgciIsInhwYXRoIjoiID5YUEFUSD4gaWQoXCJtYWluLWlmcmFtZVwiKT5GUkFNRT4gPlhQQVRIPiAvaHRtbFsxXS9ib2R5WzFdL2RpdltAY2xhc3M9XCJjb250YWluZXJcIl0vZGl2W0BjbGFzcz1cImNvbnRhaW5lci1pbm5lclwiXS9kaXZbQGNsYXNzPVwibWFpblwiXS9kaXZbQGNsYXNzPVwibWFpbi1pbm5lclwiXS9kaXZbQGNsYXNzPVwiZXJyb3ItY29udGVudFwiXS9kaXZbQGNsYXNzPVwiY2FwdGNoYVwiXS9kaXZbQGNsYXNzPVwiZm9ybV9jb250YWluZXJcIl0vZGl2W0BjbGFzcz1cImctcmVjYXB0Y2hhXCJdL2RpdlsxXS9kaXZbMV0vaWZyYW1lWzFdPkZSQU1FPiA+WFBBVEg+IGlkKFwicmVjYXB0Y2hhLWFuY2hvclwiKS9kaXZbQGNsYXNzPVwicmVjYXB0Y2hhLWNoZWNrYm94LWJvcmRlclwiXSIsImF0IjoiMzgyLCAyMTQiLCJ3ZSI6dHJ1ZSwiZmEiOnRydWV9fQ==*/
      /*Browser*/
      _SELECTOR = " \u003eCSS\u003e #main-iframe\u003eFRAME\u003e \u003eCSS\u003e :nth-child(1) \u003e :nth-child(1) \u003e div \u003e iframe\u003eFRAME\u003e \u003eCSS\u003e #recaptcha-anchor \u003e :nth-child(1)";
      wait_element_visible(_SELECTOR)!
      _call(_random_point, {})!
      _if(_result().length > 0, function(){
      X = parseInt(_result().split(",")[0])
      Y = parseInt(_result().split(",")[1])
      mouse(X,Y)!
      })!
      section_end()!

      section_start("", 530195313)!
      /*Dat:eyJzIjoiUmVDYXB0Y2hhMiIsInYiOjEsImYiOltdLCJ1dyI6IjAiLCJ1dCI6IjAiLCJ1dG8iOiIwIiwidW0iOiIwIiwiZCI6W3siaWQiOiJNZXRob2QiLCJ0eXBlIjoiY29uc3RyIiwiZGF0YSI6Im1hbnVhbCIsImNsYXNzIjoic3RyaW5nIn0seyJpZCI6IlJ1Y2FwdGNoYSIsInR5cGUiOiJjb25zdHIiLCJkYXRhIjoiYTA4NGZhZDNjMGQ3MTE0NjUyZjFiODllNDE5MTdiMmMiLCJjbGFzcyI6InN0cmluZyJ9LHsiaWQiOiJUaW1lc1RvU29sdmUiLCJ0eXBlIjoiY29uc3RyIiwiZGF0YSI6IjEwIiwiY2xhc3MiOiJpbnQifSx7ImlkIjoiU2VydmVyIiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiIiLCJjbGFzcyI6InN0cmluZyJ9LHsiaWQiOiJUYXNrcyIsInR5cGUiOiJjb25zdHIiLCJkYXRhIjoiIiwiY2xhc3MiOiJzdHJpbmcifSx7ImlkIjoiU2VuZFByb3h5IiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiJmYWxzZSIsImNsYXNzIjoic3RyaW5nIn0seyJpZCI6IkNoZWNrIiwidHlwZSI6ImNoZWNrIiwiZGF0YSI6ZmFsc2V9XSwicCI6eyJpc19pbWFnZSI6ZmFsc2UsImNzcyI6IiA+Q1NTPiAjbWFpbi1pZnJhbWU+RlJBTUU+ID5DU1M+IDpudGgtY2hpbGQoMykgPiA6bnRoLWNoaWxkKDEpIiwidmVyc2lvbiI6IjEuMCIsImNzczEiOiIgPkNTUz4gI21haW4taWZyYW1lPkZSQU1FPiA+Q1NTPiA6bnRoLWNoaWxkKDMpID4gOm50aC1jaGlsZCgxKSIsImNzczIiOiIgPkNTUz4gaWZyYW1lPkZSQU1FPiA+Q1NTPiA6bnRoLWNoaWxkKDMpID4gOm50aC1jaGlsZCgxKSIsImNzczMiOiIiLCJjdXJyZW50IjoiY3NzIiwibWF0Y2giOiI+TUFUQ0g+PGlmcmFtZSBpZD1cIm1haW4taWZyYW1lXCIgc3JjPVwiL19JbmNhcHN1bD5GUkFNRT4+TUFUQ0g+PGRpdiBzdHlsZT1cIndpZHRoOiAxMDAlOyBoZWlnaHQ6IDEwMCU7IHAiLCJ4cGF0aCI6IiA+WFBBVEg+IGlkKFwibWFpbi1pZnJhbWVcIik+RlJBTUU+ID5YUEFUSD4gL2h0bWxbMV0vYm9keVsxXS9kaXZbMl0vZGl2WzFdIiwiYXQiOiI0MDIsIDEzIiwid2UiOnRydWUsImZhIjp0cnVlfX0=*/
      /*Browser*/
      BAS_SolveRecaptcha_Method = "manual";
      BAS_SolveRecaptcha_Rucaptcha = "a084fad3c0d7114652f1b89e41917b2c";
      BAS_SolveRecaptcha_Serverurl = "";
      BAS_SolveRecaptcha_Query = " \u003eCSS\u003e #main-iframe\u003eFRAME\u003e \u003eCSS\u003e :nth-child(3) \u003e :nth-child(1)";
      BAS_SolveRecaptcha_Task_List = "";
      BAS_SolveRecaptcha_Disableemulation = false;
      BAS_SolveRecaptcha_SendProxy = ("false") == "true";
      _SELECTOR = BAS_SolveRecaptcha_Query;
      BAS_SolveRecaptcha_Waiter = function()
      {
      _SELECTOR = " \u003eCSS\u003e #main-iframe\u003eFRAME\u003e \u003eCSS\u003e :nth-child(3) \u003e :nth-child(1)";
      wait_element(_SELECTOR)!
      };
      BAS_SolveRecaptcha_Path = function(){return (get_element_selector(_SELECTOR, false))};
      BAS_SolveRecaptcha_TimeToSolve = 10;
      _call(BAS_SolveRecaptcha,null)!
      section_end()!

      section_start("", 219216870)!
      /*Dat:eyJzIjoiY2xpY2tDYXB0Y2hhRWxlbWVudCIsInYiOjEsImYiOltdLCJ1dyI6IjAiLCJ1dCI6IjAiLCJ1dG8iOiIwIiwidW0iOiIwIiwiZCI6W3siaWQiOiJzZXJ2aWNlTmFtZSIsInR5cGUiOiJjb25zdHIiLCJkYXRhIjoicnVjYXB0Y2hhIiwiY2xhc3MiOiJzdHJpbmcifSx7ImlkIjoic2VydmljZUtleSIsInR5cGUiOiJjb25zdHIiLCJkYXRhIjoiYTA4NGZhZDNjMGQ3MTE0NjUyZjFiODllNDE5MTdiMmMiLCJjbGFzcyI6InN0cmluZyJ9LHsiaWQiOiJ0ZXh0SW5zdHJ1Y3Rpb25zIiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiIiLCJjbGFzcyI6InN0cmluZyJ9LHsiaWQiOiJlbXVsYXRlTW91c2UiLCJ0eXBlIjoiY2hlY2siLCJkYXRhIjp0cnVlfSx7ImlkIjoidGFza1dhaXRUaW1lb3V0IiwidHlwZSI6ImNvbnN0ciIsImRhdGEiOiI1MDAwIiwiY2xhc3MiOiJpbnQifSx7ImlkIjoidGFza1dhaXREZWxheSIsInR5cGUiOiJjb25zdHIiLCJkYXRhIjoiNTAwMCIsImNsYXNzIjoiaW50In0seyJpZCI6InNlcnZpY2VVcmwiLCJ0eXBlIjoiY29uc3RyIiwiZGF0YSI6IiIsImNsYXNzIjoic3RyaW5nIn1dLCJwIjp7ImlzX2ltYWdlIjpmYWxzZSwiY3NzIjoiID5DU1M+ICNtYWluLWlmcmFtZT5GUkFNRT4gPkNTUz4gOm50aC1jaGlsZCg0KSA+IGlmcmFtZT5GUkFNRT4gPkNTUz4gI3JjLWltYWdlc2VsZWN0IiwidmVyc2lvbiI6IjEuMCIsImNzczEiOiIgPkNTUz4gI21haW4taWZyYW1lPkZSQU1FPiA+Q1NTPiA6bnRoLWNoaWxkKDQpID4gaWZyYW1lPkZSQU1FPiA+Q1NTPiAjcmMtaW1hZ2VzZWxlY3QiLCJjc3MyIjoiID5DU1M+IGlmcmFtZT5GUkFNRT4gPkNTUz4gOm50aC1jaGlsZCg0KSA+IGlmcmFtZT5GUkFNRT4gPkNTUz4gYm9keSA+IDpudGgtY2hpbGQoMykgPiA6bnRoLWNoaWxkKDEpIiwiY3NzMyI6IiIsImN1cnJlbnQiOiJjc3MiLCJtYXRjaCI6Ij5NQVRDSD48aWZyYW1lIGlkPVwibWFpbi1pZnJhbWVcIiBzcmM9XCIvX0luY2Fwc3VsPkZSQU1FPj5NQVRDSD48aWZyYW1lIHRpdGxlPVwicmVjYXB0Y2hhIGNoYWxsZW5nZSBleHBpcj5GUkFNRT4+TUFUQ0g+PGRpdiBpZD1cInJjLWltYWdlc2VsZWN0XCIgYXJpYS1tb2RhbD1cInRydSIsInhwYXRoIjoiID5YUEFUSD4gaWQoXCJtYWluLWlmcmFtZVwiKT5GUkFNRT4gPlhQQVRIPiAvaHRtbFsxXS9ib2R5WzFdL2RpdlsyXS9kaXZbNF0vaWZyYW1lWzFdPkZSQU1FPiA+WFBBVEg+IGlkKFwicmMtaW1hZ2VzZWxlY3RcIikiLCJhdCI6IjQwNSwgMTUiLCJ3ZSI6dHJ1ZSwiZmEiOnRydWV9fQ==*/
      /*Browser*/
      _call_function(BASCaptchaSolver.solveCoordinatesCaptcha, {
      textInstructions: "",
      taskWaitTimeout: 5000,
      taskWaitDelay: 5000,
      emulateMouse: true,
      serviceName: "rucaptcha",
      serviceUrl: "",
      serviceKey: "a084fad3c0d7114652f1b89e41917b2c",
      query: " \u003eCSS\u003e #main-iframe\u003eFRAME\u003e \u003eCSS\u003e :nth-child(4) \u003e iframe\u003eFRAME\u003e \u003eCSS\u003e #rc-imageselect",
      waiter: function () {
      _SELECTOR = " \u003eCSS\u003e #main-iframe\u003eFRAME\u003e \u003eCSS\u003e :nth-child(4) \u003e iframe\u003eFRAME\u003e \u003eCSS\u003e #rc-imageselect";
      wait_element(_SELECTOR)!
      },
      path: function () {
      return (get_element_selector(_SELECTOR, false));
      },
      })!
      section_end()!

   })!
   section_end()!

})!]]></Script>
     <ModuleInfo><![CDATA[{
}
]]></ModuleInfo>
     <Modules/>
     <EmbeddedData><![CDATA[[]]]></EmbeddedData>
     <DatabaseId>Database.11532</DatabaseId>
     <Schema></Schema>
     <ConnectionIsRemote>false</ConnectionIsRemote>
     <ConnectionServer></ConnectionServer>
     <ConnectionPort></ConnectionPort>
     <ConnectionLogin></ConnectionLogin>
     <ConnectionPassword></ConnectionPassword>
     <ScriptName>ScriptName</ScriptName>
     <ProtectionStrength>4</ProtectionStrength>
     <UnusedModules>Path;PhoneVerification;String;URL;InMail;JSON</UnusedModules>
     <ScriptIcon>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</ScriptIcon>
     <IsCustomIcon>false</IsCustomIcon>
     <HideBrowsers>false</HideBrowsers>
     <IntegrateScheduler>false</IntegrateScheduler>
     <SingleInstance>false</SingleInstance>
     <CopySilent>false</CopySilent>
     <IsEnginesInAppData>false</IsEnginesInAppData>
     <CompileType>NoProtection</CompileType>
     <ScriptVersion>1.0.0</ScriptVersion>
     <AvailableLanguages>en,ru</AvailableLanguages>
     <EngineVersion>25.3.8</EngineVersion>
     <SettingsWorker>EnableFlash=false
EnableWidevine=false
AutostartDebug=false
SaveBrowserLog=false
ProfilesCaching=true
ToolboxHeight=300
MaxBrowserStartSimultaneously=3
MinFreeMemoryToStartBrowser=1500
MinUnusedCpu=35
ScenarioWidth=500
Zoom=100
IsMaximized=true
Restart=true
UseHumanLikeMouseMoves=true
DebugToolbox=false
DebugScenario=false
Languages=&quot;&quot;
Modules=&quot;&quot;
Canvas=&quot;enable&quot;
CanvasNoise=&quot;&quot;
Audio=&quot;enable&quot;
QUIC=&quot;disable&quot;
AudioNoise=&quot;&quot;
MaxFPS=30
Webrtc=&quot;enable&quot;
WebrtcIps=&quot;&quot;
Webgl=&quot;enable&quot;
WebglNoise=&quot;&quot;
WebglRenderer=&quot;&quot;
WebglVendor=&quot;&quot;
Detector=true
</SettingsWorker>
     <ChromeCommandLine>--disk-cache-size=1
--disable-gpu-program-cache
--disable-gpu-shader-disk-cache
--disable-component-update
--disable-features=GpuProcessHighPriorityWin,GpuUseDisplayThreadPriority
--enable-features=ViewportHeightClientHintHeader
--lang=en
--disable-auto-reload
--reduce-user-agent-minor-version</ChromeCommandLine>
     <ModulesMetaJson>{
    &quot;Archive&quot;: false,
    &quot;Checksum&quot;: false,
    &quot;Excel&quot;: false,
    &quot;FTP&quot;: false,
    &quot;FunCaptcha&quot;: false,
    &quot;HCaptcha&quot;: false,
    &quot;MailDeprecated&quot;: false,
    &quot;ReCaptcha&quot;: true,
    &quot;SQL&quot;: false,
    &quot;SmsReceive&quot;: false
}
</ModulesMetaJson>
     <InterfaceState>{&quot;variables&quot;:{&quot;sortings&quot;:[{&quot;name&quot;:&quot;frequency&quot;,&quot;active&quot;:false},{&quot;name&quot;:&quot;dateModified&quot;,&quot;active&quot;:false},{&quot;name&quot;:&quot;dateCreated&quot;,&quot;active&quot;:false},{&quot;name&quot;:&quot;alphabetically&quot;,&quot;active&quot;:true}],&quot;filters&quot;:[{&quot;name&quot;:&quot;undefined&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;boolean&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;object&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;string&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;number&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;array&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;date&quot;,&quot;active&quot;:true},{&quot;name&quot;:&quot;null&quot;,&quot;active&quot;:true}],&quot;options&quot;:[{&quot;name&quot;:&quot;groups&quot;,&quot;active&quot;:false}],&quot;groups&quot;:[{&quot;id&quot;:0,&quot;name&quot;:&quot;Main&quot;,&quot;color&quot;:&quot;brown&quot;,&quot;expanded&quot;:true,&quot;items&quot;:[{&quot;key&quot;:&quot;IS_EXISTS&quot;,&quot;fixed&quot;:false}]}],&quot;nodes&quot;:{}},&quot;resources&quot;:{&quot;sortings&quot;:[],&quot;filters&quot;:[],&quot;options&quot;:[],&quot;groups&quot;:[{&quot;id&quot;:0,&quot;name&quot;:&quot;Main&quot;,&quot;color&quot;:&quot;brown&quot;,&quot;expanded&quot;:true,&quot;items&quot;:[{&quot;key&quot;:&quot;proxy&quot;,&quot;fixed&quot;:false},{&quot;key&quot;:&quot;wallet&quot;,&quot;fixed&quot;:false}]}],&quot;nodes&quot;:{}},&quot;callstack&quot;:{&quot;filters&quot;:[]}}</InterfaceState>
     <OutputTitle1 en="First Results" ru="First Results"/>
     <OutputTitle2 en="Second Results" ru="Second Results"/>
     <OutputTitle3 en="Third Results" ru="Third Results"/>
     <OutputTitle4 en="Fourth Results" ru="Fourth Results"/>
     <OutputTitle5 en="Fifth Results" ru="Fifth Results"/>
     <OutputTitle6 en="Sixth Results" ru="Sixth Results"/>
     <OutputTitle7 en="Seventh Results" ru="Seventh Results"/>
     <OutputTitle8 en="Eighth Results" ru="Eighth Results"/>
     <OutputTitle9 en="Ninth Results" ru="Ninth Results"/>
     <OutputVisible1>1</OutputVisible1>
     <OutputVisible2>1</OutputVisible2>
     <OutputVisible3>1</OutputVisible3>
     <OutputVisible4>0</OutputVisible4>
     <OutputVisible5>0</OutputVisible5>
     <OutputVisible6>0</OutputVisible6>
     <OutputVisible7>0</OutputVisible7>
     <OutputVisible8>0</OutputVisible8>
     <OutputVisible9>0</OutputVisible9>
     <ModelList>
          <Model>
               <Name>proxy</Name>
               <Description en="proxy" ru="proxy"/>
               <SectionName ru=""/>
               <VisibilityConditionValue></VisibilityConditionValue>
               <VisibilityConditionVariable></VisibilityConditionVariable>
               <Type>LinesFromFile</Type>
               <IsAdvanced>0</IsAdvanced>
               <Visible>1</Visible>
               <Enabled>1</Enabled>
               <AllowedTypes>LinesFromFile</AllowedTypes>
               <Filename></Filename>
               <Clean>0</Clean>
               <Read>1</Read>
               <Mix>0</Mix>
               <MaxSuccess>10</MaxSuccess>
               <MaxFail>10</MaxFail>
               <MaxSimultaneous>1</MaxSimultaneous>
               <Interval>5000</Interval>
               <ReloadInterval>0</ReloadInterval>
               <RenewInterval>-1</RenewInterval>
               <Greedy>0</Greedy>
          </Model>
          <Defaults/>
          <Model>
               <Name>wallet</Name>
               <Description en="wallet" ru="wallet"/>
               <SectionName ru=""/>
               <VisibilityConditionValue></VisibilityConditionValue>
               <VisibilityConditionVariable></VisibilityConditionVariable>
               <Type>LinesFromFile</Type>
               <IsAdvanced>0</IsAdvanced>
               <Visible>1</Visible>
               <Enabled>1</Enabled>
               <AllowedTypes>LinesFromFile</AllowedTypes>
               <Filename></Filename>
               <Clean>0</Clean>
               <Read>1</Read>
               <Mix>0</Mix>
               <MaxSuccess>1</MaxSuccess>
               <MaxFail>1</MaxFail>
               <MaxSimultaneous>1</MaxSimultaneous>
               <Interval>5000</Interval>
               <ReloadInterval>0</ReloadInterval>
               <RenewInterval>-1</RenewInterval>
               <Greedy>0</Greedy>
          </Model>
          <Defaults/>
     </ModelList>
</BrowserAutomationStudioProject>
