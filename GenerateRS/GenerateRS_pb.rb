# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GenerateRS.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_file("GenerateRS.proto", :syntax => :proto3) do
    add_message "AppleRemoteAuth.RemoteDeviceInfo" do
      optional :rq_data, :bytes, 1
      optional :rq_sig_data, :bytes, 2
      optional :grappa_session_id, :uint32, 3
      optional :fair_play_certificate, :bytes, 5
      optional :fair_device_type, :int64, 6
      optional :fair_play_guid, :string, 8
      proto3_optional :grappa, :bytes, 9
      proto3_optional :dsid, :int64, 10
      proto3_optional :keyTypeSupportVersion, :int64, 11
    end
    add_message "AppleRemoteAuth.rsdata" do
      optional :rs_data, :bytes, 1
      optional :ret, :bool, 2
      proto3_optional :rs_sig_data, :bytes, 3
    end
    add_message "AppleRemoteAuth.Grappa" do
      optional :grappaData, :bytes, 1
      optional :grappa_session_id, :uint32, 2
      optional :ret, :bool, 3
    end
    add_message "AppleRemoteAuth.rqGeneGrappa" do
      optional :udid, :string, 1
    end
    add_message "AppleRemoteAuth.scinfo" do
      optional :appleid, :string, 1
      optional :dsid, :int64, 2
      optional :hardwareInfo, :bytes, 3
      optional :sidb, :bytes, 4
      optional :sidd, :bytes, 5
    end
    add_message "AppleRemoteAuth.rsscinfo" do
      optional :ret, :bool, 1
    end
  end
end

module AppleRemoteAuth
  RemoteDeviceInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.RemoteDeviceInfo").msgclass
  Rsdata = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.rsdata").msgclass
  Grappa = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.Grappa").msgclass
  RqGeneGrappa = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.rqGeneGrappa").msgclass
  Scinfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.scinfo").msgclass
  Rsscinfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("AppleRemoteAuth.rsscinfo").msgclass
end
