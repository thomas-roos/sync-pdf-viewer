# AWS IoT Core Setup for MQTT PDF Sync

## Prerequisites
1. AWS Account with IoT Core access
2. AWS CLI configured (optional but recommended)

## Step 1: Create IoT Core Resources

### 1.1 Create an IoT Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect",
        "iot:Subscribe",
        "iot:Publish",
        "iot:Receive"
      ],
      "Resource": [
        "arn:aws:iot:*:*:client/pdf-viewer-*",
        "arn:aws:iot:*:*:topic/pdf-sync/*",
        "arn:aws:iot:*:*:topicfilter/pdf-sync/*"
      ]
    }
  ]
}
```

### 1.2 Create IoT Thing (Optional)
- Go to AWS IoT Console > Manage > Things
- Create a new thing called "pdf-sync-system"

### 1.3 Get Your IoT Endpoint
```bash
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

## Step 2: Authentication Options

### Option A: Using IAM User (Simpler for testing)
1. Create IAM user with IoT permissions
2. Generate access keys
3. Use access keys in the web app

### Option B: Using Cognito (Recommended for production)
1. Create Cognito Identity Pool
2. Configure unauthenticated access with IoT permissions
3. Use Cognito credentials in web app

## Step 3: Configure the Web App

1. Update `mqttEndpoint` with your IoT endpoint
2. Set up authentication (access keys or Cognito)
3. Customize local folder options
4. Set your MQTT topic (default: `pdf-sync/folder-selection`)

## Step 4: Folder Structure

Organize your files like this on each device:
```
/your-web-app/
├── mqtt-pdf-viewer.html
├── mobile1/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
├── mobile2/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
├── tablet1/
│   └── ...
└── desktop/
    └── ...
```

## Usage Flow

1. **Server/Controller Device**: 
   - Connects to MQTT
   - Publishes PDF filename to topic
   - Example: `{"pdfName": "sermon-2024-01-07.pdf", "deviceName": "server"}`

2. **Client Devices** (mobiles, tablets):
   - Connect to same MQTT topic
   - Receive PDF filename
   - Load PDF from their local folder
   - Each device loads: `{localFolder}/{receivedPdfName}`

## Security Considerations

- Use Cognito Identity Pools for production
- Implement proper IAM policies
- Consider using certificate-based authentication
- Enable CloudWatch logging for monitoring

## Troubleshooting

- Check IoT Core logs in CloudWatch
- Verify endpoint URL format
- Ensure proper IAM permissions
- Test MQTT connection with AWS IoT Device Simulator first
