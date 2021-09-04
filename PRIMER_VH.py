import pymem
import pymem.process
import requests

dwClientState = 5828580
dwClientState_GetLocalPlayer = 384
dwClientState_IsHLTV = 19784
dwClientState_Map = 652
dwClientState_MapDirectory = 392
dwClientState_MaxPlayer = 904
dwClientState_PlayerInfo = 21184
dwClientState_State = 264
dwClientState_ViewAngles = 19856
dwEntityList = 81407604
dwForceAttack = 52249604
dwForceAttack2 = 52249616
dwForceBackward = 52249532
dwForceForward = 52249544
dwForceJump = 86298068
dwForceLeft = 52249568
dwForceRight = 52249556
dwGameDir = 6477816
dwGameRulesProxy = 86769852
dwGetAllClasses = 14364012
dwGlobalVars = 5827816
dwGlowObjectManager = 86946936
dwInput = 85935192
dwInterfaceLinkList = 9722436
dwLocalPlayer = 14201516
dwMouseEnable = 14224976
dwMouseEnablePtr = 14224928
dwPlayerResource = 52242224
dwRadarBase = 85818348
dwSensitivity = 14224620
dwSensitivityPtr = 14224576
dwSetClanTag = 565664
dwViewMatrix = 81348468
dwWeaponTable = 85937944
dwWeaponTableIndex = 12892
dwYawPtr = 14224048
dwZoomSensitivityRatioPtr = 14245200
dwbSendPackets = 881610
dwppDirect3DDevice9 = 684112
m_fFlags = 0x104
m_iGlowIndex = 42040
m_iTeamNum = 244

try:
    print("neverlose bender has launched.") # название нашего сообщества для создания читиков
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
except pymem.exception.ProcessNotFound:
    print("индус писал что ли")
    quit()

def vh():
    while True:
        glowManager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1, 60):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entityTeamId = pm.read_int(entity + m_iTeamNum)
                entityGlow = pm.read_int(entity + m_iGlowIndex)

                if entityTeamId == 3:  # Counter-terrorist КОНТЕР-ТЕРРОССИТ ВИН
                    # цвета менять во флоут
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x4, float(1))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x8, float(0))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0xC, float(1))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x10, float(1))
                    pm.write_int(glowManager + entityGlow * 0x38 + 0x24, 1)
                elif entityTeamId == 2:  # Terrorist ПЛЕН ИЗ ЗЕ БОМБ
                    # цвета менять во флоут
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x4, float(0))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x8, float(1))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0xC, float(1))
                    pm.write_float(glowManager + entityGlow * 0x38 + 0x10, float(1))
                    pm.write_int(glowManager + entityGlow * 0x38 + 0x24, 1)
vh()