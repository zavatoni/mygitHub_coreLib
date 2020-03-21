#!/usr/bin/python3
# -*- coding:UTF-8 -*-
from rootModule import vsphereSDK
from corresPond_4layer.indexKey_module import correspond
from warnEach_layerPacker.dataCenter_layer import triggered_AlarmState
from each_layerInfo_packer.dataCenter_layer import centerSummary
from each_layerInfo_packer.hostCluster_layer import vimclusterStatus
from each_layerInfo_packer.esxi_vimHost_layer import esxiSum
from each_layerInfo_packer.vmGuest_layer import vmGuestsummary
from each_layerInfo_packer.networkInfo_layer import netWork
from pandas import DataFrame
from pandas import ExcelWriter
from time import strftime


class outExcel():
    def __init__(self):
        self.setVar = vsphereSDK()

    def correspondStore(self):
        setVar = correspond()
        self.setVar.yamlPath(
            setType=setVar.clusterTo_esxi(),
            setName='data/vimCluster_vimHost.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.clusterTo_virtHost(),
            setName='data/vimCluster_vmGuest.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.esxiTO_virtualHost(),
            setName='data/vimHost_vmGuest.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.dataCenter_to_Cluster_esxi(),
            setName='data/dataCenter_vimCluster_vimHost.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.dataCenter_to_Cluster(),
            setName='data/dataCenter_vimCluster.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.dataCenter_to_Cluster_to_esxi_vmGuest(),
            setName='data/dataCenter_vimCluster_vmGuest.yml'
        )
        self.setVar.yamlPath(
            setType=setVar.dataCenter_to_vmGuest(),
            setName='data/dataCenter_vmGuest.yml'
        )

    def warningView(self):
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                set_obj0 = DataFrame.from_dict(triggered_AlarmState().dataCenter_warn()).T
                set_obj1 = DataFrame.from_dict(triggered_AlarmState().vimHost_warn()).T
                set_obj2 = DataFrame.from_dict(triggered_AlarmState().vimCluster_warn()).T.append(set_obj1, sort=False)
                with ExcelWriter(self.setVar.formatPatch(
                        pathStyle="dataWarn\/vsphere{}Warn_{}info.xlsx".format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name']
                        )
                )
                ) as object_f:
                    set_obj0.to_excel(object_f, sheet_name="dataCenter warning Info")
                    set_obj2.to_excel(object_f, sheet_name="esxi And cluster Warn Info")
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle="dataWarn/vsphere{}Warn_{}info.xlsx".format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name']
                        )
                    )
                )

    def warningEx_info(self):
        pass
    def get_netWork_vswitch(self):
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                netBaseobj=DataFrame.from_dict(netWork().networkBase()).T
                getBaseobj=DataFrame.from_dict(netWork().get_Switchs_base()).T
                getPnicobj=DataFrame.from_dict(netWork().get_Switchs_pnics()).T
                getPortgroupObj=DataFrame.from_dict(netWork().get_Switchs_portgroup()).T
                getvSwitchobj=DataFrame.from_dict(netWork().get_Switchs_vswitch()).T
                getVnicobj=DataFrame.from_dict(netWork().get_Switchs_vnics()).T
                with ExcelWriter(
                        self.setVar.formatPatch(
                            pathStyle='dataSum\/netVswitch{}_Sum{}info.xlsx'.format(
                                strftime("%Y%m%d-%H"),
                                readConfig.get(readKey)['name']
                            )
                        )
                ) as object_f:
                    netBaseobj.to_excel(object_f,sheet_name='netWork Base Case')
                    getBaseobj.to_excel(object_f,sheet_name='switch Base Case')
                    getVnicobj.to_excel(object_f,sheet_name='switch vnic case')
                    getPnicobj.to_excel(object_f,sheet_name='switch pnic case')
                    getPortgroupObj.to_excel(object_f,sheet_name='switch portGroup case')
                    getvSwitchobj.to_excel(object_f,sheet_name='vSwitch object case')
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle="dataSum/netVswitch{}_Sum{}info.xlsx".format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name'])
                    )
                )


    def dataCenterView(self):
        # 'summary_4Layerpacker/dataStore'
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                networkFrame = DataFrame.from_dict(centerSummary().netWork()).T
                parentFrame = DataFrame.from_dict(centerSummary().parent()).T
                storeFrame = DataFrame.from_dict(centerSummary().dataStore()).T
                setFrame = DataFrame.from_dict(centerSummary().networkFolder()).T
                folderFrame = DataFrame.from_dict(centerSummary().datastoreFolder()).T.append(setFrame, sort=False)
                with ExcelWriter(
                        self.setVar.formatPatch(
                            pathStyle='dataSum\/dataCenter{}_Sum{}info.xlsx'.format(
                                strftime("%Y%m%d-%H"),
                                readConfig.get(readKey)['name']
                            )
                        )
                ) as object_f:
                    networkFrame.to_excel(object_f, sheet_name='netWork Summary case')
                    storeFrame.to_excel(object_f, sheet_name='dataStore Summary case')
                    parentFrame.to_excel(object_f, sheet_name='parent Summary case')
                    folderFrame.to_excel(object_f, sheet_name='base Summary case')
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle="dataSum/dataCenter{}_Sum{}info.xlsx".format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name'])
                    )
                )

    def clusterView(self):
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                storeObject = DataFrame.from_dict(vimclusterStatus().dataStore()).T
                parentObject = DataFrame.from_dict(vimclusterStatus().parent()).T
                poolObject = DataFrame.from_dict(vimclusterStatus().resourcePool()).T.append(parentObject, sort=False)
                netObject = DataFrame.from_dict(vimclusterStatus().networkInfo()).T.append(storeObject, sort=False)
                sumObject = DataFrame.from_dict(vimclusterStatus().summary()).T
                sysObject = DataFrame.from_dict(vimclusterStatus().systemInfo()).T.append(poolObject, sort=False)
                hciObject = DataFrame.from_dict(vimclusterStatus().hciConfig()).T
                with ExcelWriter(
                        self.setVar.formatPatch(
                            pathStyle="dataSum/vimCluster{}_{}_info.xlsx".format(
                                strftime("%Y%m%d-%H"),
                                readConfig.get(readKey)['name']
                            )
                        )

                ) as object_f:
                    netObject.to_excel(object_f, sheet_name="netWork&store case")
                    sysObject.to_excel(object_f, sheet_name="system&pool&parent case")
                    sumObject.to_excel(object_f, sheet_name="vimCluster summary case")
                    hciObject.to_excel(object_f, sheet_name="vimCluster hciConfig case")
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle="dataSum/vimCluster{}_{}_info.xlsx".format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name']
                        )
                    )

                )

    def esxiView(self):
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                esxiFrame = DataFrame.from_dict(esxiSum().configInfo()).T
                esxiData = DataFrame.from_dict(esxiSum().hardwareInfo()).T
                esxiExcel = DataFrame.from_dict(esxiSum().runtimeInfo()).T
                esxiWriter = DataFrame.from_dict(esxiSum().runtime_networkRuntimeInfo_netStackInstanceRuntimeInfo()).T
                esxiPandas = DataFrame.from_dict(esxiSum().runtime_vsanRuntime_membershipListInfo()).T
                esxiStr = DataFrame.from_dict(esxiSum().runtime_healthSystemRuntime_hardwareStatusInfo()).T
                with ExcelWriter(
                        self.setVar.formatPatch(
                            pathStyle='dataSum/vimHost{}_{}_info.xlsx'.format(
                                strftime("%Y%m%d-%H"),
                                readConfig.get(readKey)['name']
                            )
                        )
                ) as strf:
                    esxiData.to_excel(strf, sheet_name='hardware info')
                    esxiFrame.to_excel(strf, sheet_name='config info')
                    esxiExcel.to_excel(strf, sheet_name='runtime info')
                    esxiWriter.to_excel(strf, sheet_name='runtime networkRuntimeinfo netStackInstanceRuntimeInfo')
                    esxiPandas.to_excel(strf, sheet_name='runtime vsanRuntime membershipListInfo')
                    esxiStr.to_excel(strf, sheet_name='runtime healthSystemRuntime hardwareStatusInfo')
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle='dataSum/vimHost{}_{}_info.xlsx'.format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name']
                        )
                    )
                )

    def vimGuestView(self):
        readConfig = self.setVar.vsphereConfig(configStr='Conf\Account.yml')
        for readKey in readConfig.keys():
            if len(readConfig.get(readKey)) > 0:
                vmGuest_runtime = DataFrame.from_dict(vmGuestsummary().runtimeBase()).T
                vmGuest_guest = DataFrame.from_dict(vmGuestsummary().guestBase()).T
                vmGuest_config = DataFrame.from_dict(vmGuestsummary().configBase()).T
                vmGuest_storage = DataFrame.from_dict(vmGuestsummary().storageBase()).T
                vmGuest_quickStats = DataFrame.from_dict(vmGuestsummary().quickStatsBase()).T
                vmGuest_network = DataFrame.from_dict(vmGuestsummary().networkBase()).T
                with ExcelWriter(
                        self.setVar.formatPatch(
                            pathStyle='dataSum/vmGuest{}_{}_info.xlsx'.format(
                                strftime("%Y%m%d-%H"),
                                readConfig.get(readKey)['name']
                            )
                        )
                ) as gf:
                    vmGuest_config.to_excel(gf, sheet_name='configure BaseInfo')
                    vmGuest_runtime.to_excel(gf, sheet_name='runtime BaseInfo')
                    vmGuest_guest.to_excel(gf, sheet_name='guest BaseInfo')
                    vmGuest_storage.to_excel(gf, sheet_name='storage BaseInfo')
                    vmGuest_quickStats.to_excel(gf, sheet_name='quickStats BaseInfo')
                    vmGuest_network.to_excel(gf, sheet_name='netWork Base Info')
                self.setVar.sheetTable_Style(
                    ex_str=self.setVar.formatPatch(
                        pathStyle='dataSum/vmGuest{}_{}_info.xlsx'.format(
                            strftime("%Y%m%d-%H"),
                            readConfig.get(readKey)['name']
                        )
                    )
                )


def main():
    outVar = outExcel()
    # setVar = vsphereSDK()
    outVar.correspondStore()
    outVar.warningView()
    outVar.get_netWork_vswitch()
    # outVar.warningEx_info()
    outVar.dataCenterView()
    outVar.clusterView()
    outVar.esxiView()
    outVar.vimGuestView()
    # setFile=vsphereSDK().formatPatch(
    #     pathStyle='dataWarn/vsphere{}Warninfo.xlsx'.format(strftime("%Y%m%d-%H"))
    # )
    # print(setFile)


if __name__ == '__main__':
    main()
