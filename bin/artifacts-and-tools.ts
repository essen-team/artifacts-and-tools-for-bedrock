#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { StackConfig } from "../lib/types";
import { ArtifactsAndToolsStack } from "../lib/stack";

const config: StackConfig = {
  bedrockRegion: "us-west-2",
  //bedrockModel: "anthropic.claude-3-sonnet-20240229-v1:0",
  bedrockModel: "anthropic.claude-3-5-sonnet-20241022-v2:0",
  playground: {
    enabled: true,
  },
  artifacts: {
    enabled: true,
  },
  codeInterpreterTool: {
    enabled: true,
  },
  webSearchTool: {
    enabled: true,
  },
};

const app = new cdk.App();
new ArtifactsAndToolsStack(app, "ArtifactsAndToolsStack", { config });
